# analysis/analyze.py (6단계: pandas 분석)

from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "expenses.csv"

df = pd.read_csv(DATA_PATH)

print("=== 원본 데이터 ===")
print(df)
print()

# 1) 전체 합계
total = df["amount"].sum()
print(f"총 지출: {total}원\n")

# 2) 카테고리별 합계
category_totals = df.groupby("category")["amount"].sum()
print("=== 카테고리별 합계 ===")
print(category_totals)
print()

# 3) 날짜별 합계 (덤)
date_totals = df.groupby("date")["amount"].sum()
print("=== 날짜별 합계 ===")
print(date_totals)