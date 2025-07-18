
import streamlit as st

st.set_page_config(page_title="利益分配計算機", layout="centered")

st.title("💰 プロジェクト利益分配計算機")

st.markdown("### 使い方")
st.markdown("プロジェクトの総利益を入力し、「計算する」ボタンを押すと、以下の割合に基づいて分配額が表示されます：")
st.markdown("- **越智さん**: 40%\n- **青木ダニエルさん**: 30%\n- **青木ケンさん**: 30%")

# 入力
ganancia_total = st.number_input("プロジェクトの総利益を入力してください（¥）", min_value=0, step=100000, format="%d")

if st.button("計算する"):
    # 計算
    ganancia_ochi = ganancia_total * 0.40
    ganancia_daniel = ganancia_total * 0.30
    ganancia_ken = ganancia_total * 0.30

    # 結果
    st.markdown("### 📊 分配結果")
    st.write(f"**越智さん (40%)**: ¥{ganancia_ochi:,.0f}")
    st.write(f"**青木ダニエルさん (30%)**: ¥{ganancia_daniel:,.0f}")
    st.write(f"**青木ケンさん (30%)**: ¥{ganancia_ken:,.0f}")
