#!python3
import math
import numpy as np


def get_scale_matrix(scale: tuple[float, float]) -> np.ndarray:
    return np.array([[scale[0], 0.0, 0.0], [0.0, scale[1], 0.0], [0.0, 0.0, 1.0]], dtype=np.float64)


def get_rotation_matrix(angle: float) -> np.ndarray:
    s = math.sin(angle)
    c = math.cos(angle)
    return np.array([[c, -s, 0.0], [s, c, 0.0], [0.0, 0.0, 1.0]], dtype=np.float64).T


def get_transform_matrix(size: int = 3) -> np.ndarray:
    """
    :param size: matrix size
    :return: matrix that have 1.0 on main diagonal and 0.0 on other positions
    """
    return np.diag(np.full(size, 1, dtype=np.float64))


def get_translation_matrix(translation: tuple[float, float]) -> np.ndarray:
    result = get_transform_matrix(3)
    result[2, :2] = translation
    return result


def modelMatrix(inMatrix: dict, sequence: str) -> tuple[float, float]:
    affine_matrix = get_transform_matrix(3)  # here we will store created matrix

    for step in sequence:
        step = step.upper()  # convert to uppercase
        if step == "S":  # scale
            affine_matrix = get_scale_matrix(inMatrix["S"]) @ affine_matrix
        elif step == "R":  # rotate
            # dont forget convert degrees to radians
            affine_matrix = get_rotation_matrix(inMatrix["R"] * math.pi / 180.0) @ affine_matrix
        else:  # translate
            affine_matrix = get_translation_matrix(inMatrix["T"]) @ affine_matrix

    # multiply vector and matrix (here we add 3rd element [1.0] to the vector because we use affine transformation)
    result_vector = np.array([*inMatrix["V"], 1.0], dtype=np.float64) @ affine_matrix

    return result_vector[0], result_vector[1]  # return result x, y


if __name__ == "__main__":
    inMatrix1 = {"S": (3.0, 1.2), "R": 33.0, "T": (1.0, 2.0), "V": (2.0, 3.0)}
    vec2_j = modelMatrix(inMatrix1, "SRT")
    print("j = vector2d(%.3f, %.3f)" % vec2_j)  # printing result using standard formatting, rounding to 3 digits

    inMatrix2 = {"S": (1.0, 1.2), "R": 16.0, "T": (1.0, 2.0), "V": (2.0, 3.0)}
    vec2_k = modelMatrix(inMatrix2, "TRS")
    print("k = vector2d(%.3f, %.3f)" % vec2_k)  # printing result using standard formatting, rounding to 3 digits
