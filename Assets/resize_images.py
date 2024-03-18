from uploadcare import Uploadcare
from uploadcare.transformations import resize_smart


def resize_images(api_key, file_id, target_width, target_height):
    """
    Resizes images to optimize file size and dimensions for use in the project.

    :param api_key: Uploadcare API key
    :param file_id: Uploadcare file ID
    :param target_width: Target width for resized image
    :param target_height: Target height for resized image
    :return: Resized image URL
    """

    # Initialize Uploadcare client
    uploadcare = Uploadcare(api_key=api_key)

    # Get file instance
    file = uploadcare.file(file_id)

    # Apply smart resize transformation
    resized_file = file.transform(
        resize_smart(width=target_width, height=target_height)
    )

    # Get resized image URL
    resized_image_url = resized_file.cdn_url

    return resized_image_url
