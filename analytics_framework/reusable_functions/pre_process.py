def analyze_data(intake_catalog_entry):
    # Load the data via intake
    try:
        df_input = catalog[intake_catalog_entry].read()
        print(f"Data loaded successfully {df_input.head()}")
    except Exception as e:
        print(f"Error loading data: {e}")
        return
