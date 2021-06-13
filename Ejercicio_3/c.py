from MT import TM


if __name__ == "__main__":
    start = "A"
    F = ["F"]
    blank = "#"
    delta = {
        "Aa": "B a R",
        "Ab": "C b R",
        "Ba": "D a R",
        "Bb": "C b R",
        "B#": "F # L",
        "C#": "F # L",
        "Da": "D a R",
        "Db": "C b R"
    }
    entrada = "aaaab"

    M = TM(start, F, blank, delta)
    M.cinta = entrada

    result = M.compute()
    M.resume(result)