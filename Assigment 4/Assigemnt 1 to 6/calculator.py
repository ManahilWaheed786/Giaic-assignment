import streamlit as st

def calculate_bmi(weight, height):
    # BMI = weight (kg) / height (m)^2
    return weight / (height ** 2)

def main():
    st.title("BMI Calculator")

    st.write("Calculate your Body Mass Index (BMI)")

    weight = st.number_input("Enter your weight in kilograms (kg):", min_value=1.0, format="%.2f")
    height = st.number_input("Enter your height in meters (m):", min_value=0.5, format="%.2f")

    if st.button("Calculate BMI"):
        if height > 0:
            bmi = calculate_bmi(weight, height)
            st.write(f"Your BMI is: {bmi:.2f}")

            if bmi < 18.5:
                st.warning("You are underweight.")
            elif 18.5 <= bmi < 24.9:
                st.success("You have a normal weight.")
            elif 25 <= bmi < 29.9:
                st.warning("You are overweight.")
            else:
                st.error("You are obese.")
        else:
            st.error("Please enter a valid height greater than 0.")

if __name__ == "__main__":
    main()
