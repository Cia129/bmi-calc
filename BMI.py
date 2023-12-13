class BMI:
    @staticmethod
    def calculate_bmi(weight, height, gender):
        bmi = (weight / (height ** 2)) * 703
        return bmi

    @staticmethod
    def determine_bmi_category(bmi):
        if bmi < 16:
            return "Extremely underweight"
        elif 16 <= bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        elif 30 <= bmi < 34.9:
            return "Obese"
        else:
            return "Severely obese"


class BMR:
    @staticmethod
    def calculate_bmr(weight, height, age, gender):
        if gender.lower() == 'male':
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        elif gender.lower() == 'female':
            bmr = 10 * weight + 6.25 * height - 5 * age + 161
        else:
            bmr = 0
        return bmr


class HealthCalculator:
    @staticmethod  # static method is just a decorator and it defines a static method in class in python. 
    def main():
        while True:
            try:
                weight = float(input("Enter your weight in lbs: "))
                height = float(input("Enter your height in inches: "))
                gender = input("Are you male or female? ").lower()

                if gender not in ['male', 'female']:
                    print("Invalid gender. Please enter 'male' or 'female'.")
                    continue

                bmi = BMI.calculate_bmi(weight, height, gender)
                bmi_category = BMI.determine_bmi_category(bmi)

                print(f"Your BMI is: {bmi:.2f}")
                print(f"Based on the data, your BMI range is: {bmi_category} and for a {gender} is determined as {bmi_category}.")

                bmr_option = input("Would you like to calculate your BMR? (yes/no): ").lower()

                if bmr_option == 'yes':
                    age = int(input("Enter your age: "))
                    bmr = BMR.calculate_bmr(weight, height, age, gender)
                    print(f"Your average calorie intake based on height, weight, and age should be around {bmr:.2f} calories per day.")
                break

            except ValueError:
                print("Invalid input. Please enter numeric values for weight, height, and age.")


if __name__ == "__main__":
    HealthCalculator.main()

#had to change the main into healthcalculator.main





