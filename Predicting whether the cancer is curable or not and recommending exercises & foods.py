def predict_cancer():
    has_cancer = input("Does the person have cancer? (yes/no): ").lower().strip()
    if has_cancer == 'yes':
        cancer_type = input("What type of cancer does the person have? (e.g., \n Breast, lung, Bladder Cancer, Breast Cancer, Colorectal Cancer, Kidney (Renal Cell) Cancer, Lung Cancer, Lymphoma, Pancreatic Cancer, Prostate Cancer, Skin Cancer, Uterine Cancer): ").lower().strip()
        stage = input(f"What stage is the {cancer_type} cancer in? (0-4): ").strip()
        curable = stage in ['0', '1', '2']
        initiation_cause = input("How did the cancer get initiated? (smoking, genetics, environmental factors, moking, radiation, viruses, cancer-causing chemicals (carcinogens), obesity, hormones, chronic inflammation, other): ").lower().strip()
        
        advice = ""
        if curable:
            advice = "Recommended exercises: Yoga, Walking, Swimming. Suggested foods: Leafy greens, Berries, Fish."
        else:
            advice = "Recommended exercises: Gentle Yoga, Breathing exercises. \nSuggested foods: Soft foods, Nutrient-dense smoothies."

        print(f"\nPrediction Summary:\n")
        print(f"The person has {cancer_type} cancer, in stage {stage}. {'It is curable.' if curable else 'It is not curable.'}")
        print(f"Initiated by: {initiation_cause}.")
        print(advice)
    elif has_cancer == 'no':
        print("Thank you & there is a need to check further if a person doesn't have cancer.")
    else:
        print("Invalid input.")

if __name__ == "__main__":
    predict_cancer()
