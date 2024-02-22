def solution(brown, yellow):
    total = brown + yellow

    for vert in range(3, total):
        if total % vert == 0:
            hori = total // vert

            if (hori - 2) * (vert - 2) == yellow:
                return [hori, vert]