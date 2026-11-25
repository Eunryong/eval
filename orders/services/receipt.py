def format_won(amount: int) -> str:
    """원 단위 정수 금액을 "12,000원" 꼴의 글로 바꾼다."""
    return f"{amount:,}원"
