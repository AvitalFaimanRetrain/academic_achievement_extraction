import pandas as pd
from openai_argumentor.openai_requests import generate_alternative_and_acronyms, generate
from acdemic_achievement_extraction.raw_data import associates, bachelor, masters, doctors, education_levels

if __name__ == '__main__':
    original_data = pd.read_json("ed_gov_skills_enrichment_input.json")

    for i, deg in enumerate([associates, bachelor, masters, doctors]):
        if i == 0:
            all_alt_df = generate_alternative_and_acronyms(deg)
        else:
            alternative_and_acronyms_df = generate_alternative_and_acronyms(deg)
            all_alt_df = pd.concat([all_alt_df, alternative_and_acronyms_df], axis=0)

    education_fields_df = generate(all_alt_df, 'education_field')
    education_fields_df = pd.merge(all_alt_df, education_fields_df, on='name', how='left')

    major_df = generate(education_fields_df, 'major')
    major_df = pd.merge(education_fields_df, major_df, on='name', how='left')

    education_levels_df = generate(major_df, 'education_level')
    education_levels_mapping = pd.DataFrame(education_levels)

    education_levels_df = pd.merge(education_levels_df, education_levels_mapping, on='education_level', how='left')
    education_levels_df = pd.merge(major_df, education_levels_df, on='name', how='left')

    final_data = pd.merge(education_levels_df, original_data, on='name', how='left')


    final_data.to_json(f"degrees_enrichment_data.json", orient="records", lines=True)
