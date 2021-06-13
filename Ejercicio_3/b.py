from MT import TM


if __name__ == "__main__":
    start = "A"
    F = ["F"]
    blank = "#"
    delta = {
        "Ax": "B x R",
        "Ay": "C y R",
        "A#": "F # L",
        "Bx": "B x R",
        "B#": "F # L",
        "Cx": "D x R",
        "Dy": "C y R",
        "Dx": "B x R",
        "D#": "F # L"
    }
    entrada = "yxy"

    M = TM(start, F, blank, delta)
    M.cinta = entrada

    result = M.compute()
    M.resume(result)