(survey_data_decoupled
     .groupby("year")
     .size()
     .plot(kind='barh', color="#00007f", figsize=(10, 10)))