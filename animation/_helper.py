import pygame

SCALE_RATIO = 2
UNIT = SCALE_RATIO * 16

class ImageProcessor:
    @staticmethod
    def process_images(images: tuple[pygame.surface.Surface], flip: bool, scaled: float) -> tuple[pygame.surface.Surface]:
        new_images = tuple(ImageProcessor.process_image(image, flip, scaled) for image in images)
        return new_images

    @staticmethod
    def process_image(image: pygame.surface.Surface, flip: bool, scaled: float) -> pygame.surface.Surface:
        new_image = image
        if flip:
            new_image = ImageProcessor.flip(new_image)
        if scaled != 1:
            new_image = ImageProcessor.resize(new_image, scaled)
        return new_image

    @staticmethod
    def resize(image: pygame.surface.Surface, scaled: float) -> pygame.surface.Surface:
        new_image = pygame.transform.scale(image, (int(image.get_width() * scaled), int(image.get_height() * scaled)))
        return new_image

    @staticmethod
    def flip(image: pygame.surface.Surface) -> pygame.surface.Surface:
        new_image = pygame.transform.flip(image, True, False)
        return new_image

class FileReader:
    @staticmethod
    def read_line(path: str):
        lines = []
        with open(path, "r") as file:
            while (line := file.readline()):
                lines.append(line[:-1])
        return lines