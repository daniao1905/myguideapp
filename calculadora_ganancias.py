
import streamlit as st

st.set_page_config(page_title="Calculadora de Ganancias del Proyecto", layout="centered")

st.title("💰 Calculadora de Distribución de Ganancias del Proyecto")

st.markdown("### Instrucciones")
st.markdown("Ingresa la ganancia total del proyecto y se calculará automáticamente cuánto recibe cada parte según los siguientes porcentajes:")
st.markdown("- **越智さん**: 40%\n- **青木ダニエルさん**: 30%\n- **青木ケンさん**: 30%")

# Input de ganancia total
ganancia_total = st.number_input("Ganancia total del proyecto (¥)", min_value=0, step=100000, format="%d")

# Porcentajes
porcentaje_ochi = 40
porcentaje_daniel = 30
porcentaje_ken = 30

# Cálculos
ganancia_ochi = ganancia_total * porcentaje_ochi / 100
ganancia_daniel = ganancia_total * porcentaje_daniel / 100
ganancia_ken = ganancia_total * porcentaje_ken / 100

# Resultados
st.markdown("### 📊 Distribución de Ganancias")
st.write(f"**越智さん (40%)**: ¥{ganancia_ochi:,.0f}")
st.write(f"**青木ダニエルさん (30%)**: ¥{ganancia_daniel:,.0f}")
st.write(f"**青木ケンさん (30%)**: ¥{ganancia_ken:,.0f}")
