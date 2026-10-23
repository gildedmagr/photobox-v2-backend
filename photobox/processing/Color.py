from PIL import Image, ImageOps, ImageEnhance

from photobox.models.ColorSettings import ColorSettings


class Color:

    @staticmethod
    def auto_contrast(img: Image):
        if img.mode in ("RGB", "L"):
            return ImageOps.autocontrast(img, cutoff=3, ignore=0)

        if img.mode in ("RGBA", "LA", "P", "PA"):
            rgba = img.convert("RGBA")
            result = ImageOps.autocontrast(rgba.convert("RGB"), cutoff=3, ignore=0)
            result.putalpha(rgba.getchannel("A"))
            return result

        return ImageOps.autocontrast(img.convert("RGB"), cutoff=3, ignore=0)

    @staticmethod
    def adjust_color(img: Image, params: ColorSettings):
        result = img
        if params.brightness != 1:
            brightness_filter = ImageEnhance.Brightness(result)
            result = brightness_filter.enhance(params.brightness)

        if params.saturation != 1:
            saturation_filter = ImageEnhance.Color(result)
            result = saturation_filter.enhance(params.saturation)

        if params.contrast != 1:
            contrast_filter = ImageEnhance.Contrast(result)
            result = contrast_filter.enhance(params.contrast)
        return result
