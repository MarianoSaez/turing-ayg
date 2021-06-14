from MT import TM


if __name__ == "__main__":
    start = "A"
    F = ["F"]
    blank = "#"
    delta = {
        "Aa": "B a R",
        "Ba": "B a R",
        "Ab": "C b R",
        "Ca": "D a R",
        "A#": "F # L",
        "B#": "F # L",
        "D#": "F # L"
    }
    entrada = "aaaa"

    M = TM(start, F, blank, delta)
    M.cinta = entrada

    result = M.compute()
    M.resume(result)