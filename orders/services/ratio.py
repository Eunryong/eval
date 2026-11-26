def per_unit(value: int, count: int) -> int:
    """value를 count로 나눈 몫. count는 1 이상이다."""
    return value // count if value >= 0 else -(-value // count)


def average(values: tuple[int, ...]) -> float:
    """values의 평균. 비어 있으면 0.0이다."""
    if not values:
        return 0.0
    return sum(values) / len(values)
