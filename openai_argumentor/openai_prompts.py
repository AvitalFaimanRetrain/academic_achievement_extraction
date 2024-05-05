ALTERNATIVE_AND_ACRONYMS_PROMPT = """
    Given an input representing a degree, extract the following fields - name, acronyms, alternative_names and 
    alternative_acronyms. 
    
    Follow these instructions:
    1.Split the input degree by "/" to separate between the degree and its alternative degrees.
    2. For each degree option, extract the name and acronyms.
    3. Check if there are any alternative names or alternative acronyms for each degree option.
    4. Create JSON objects for each degree option and combine them into a final JSON output.
    5. Make sure you don't add any alternative names if they don't appear in the input degree.
    2. If there aren't any alternative_names and alternative_acronyms mark {} under the fields of "alternative_names" 
    and "alternative_acronyms".
    3. Ignore any '*'.
    
    Based on the input degree provided below create an extraction in the following JSON format:
    {
        "name": The full name of the degree, without its acronym.
        "acronyms": Array of acronym(s) representing the degree.
        "alternative_names": Array of alternative names for the degree.
        "alternative_acronyms": Array of alternative acronyms for the degree.
    }
    
    Good output examples:
    Input: 
    degree: Bachelor of Business (B.B.)/Bachelor of Business Administration (B.B.A.)
    Output:
        {
            "name": "Bachelor of Business",
            "acronyms": "{B.B., BB}",
            "alternative_names": "{Bachelor of Business Administration}",
            "alternative_acronyms": "{B.B.A., BBA}"
        }

    Input: 
    degree: Master of City Planning (M.C.P.)/Master of City and Regional Planning (M.C.R.P./M.R.C.P.)/Master of Regional Planning (M.R.P.)
    Output:
        {
            "name": "Master of City Planning",
            "acronyms": "{M.C.P., MCP}",
            "alternative_names": "{Master of City and Regional Planning, Master of Regional Planning}",
            "alternative_acronyms": "{M.C.R.P., MCRP, M.R.C.P., MRCP, M.R.P., MRP}"
        }

    Input: 
    degree: Bachelor of Canon Law (B.C.L.)
    Output:
        {
            "name": "Bachelor of Canon Law",
            "acronyms": "{B.C.L., BCL}",
            "alternative_names": "{}",
            "alternative_acronyms": "{}"
        }
        
    Input:
    degree: "$degree"    
"""



EDUCATION_FIELD_PROMPT = """
    Given an input representing a degree please extract the education field. 

    Based on the input degree provided below create an extraction in the following JSON format (without any notes):
    {
        "name": Degree input, the same name you received in the input.
        "education_field": The education field of the degree.
    }
    
    Good output examples:
    Input: 
    degree: Associate of Applied Science in Information Technology
    Output:
        {
            "name": "Associate of Applied Science in Information Technology",
            "education_field": "Applied Science"
        }
    
    Input: 
    degree: Bachelor of Science in Occupational Therapy Assistant
    Output:
        {
            "name": "Bachelor of Science in Occupational Therapy Assistant",
            "education_field": "Science"
        }
    
    Input: 
    degree: Bachelor of Arts Major in Economics
    Output:
        {
            "name": "Bachelor of Arts Major in Economics",
            "education_field": "Liberal Arts"
        }
    
    Extract the correct education field for the following degree:
            ```
            $degree
            ```
"""

MAJOR_PROMPT = """
    Given an input representing a degree please extract the major following these instructions:
    1. If there isn't any major mark 'N/A'.
    
    Based on the input degree provided below create an extraction in the following JSON format:
    {
        "name": Degree input, the same name you received in the input
        "major": The major of the degree
    }
    
    Good output examples:
    Input: 
    degree: Associate of Applied Science in Information Technology
    Output:
        {
            "name": "Associate of Applied Science in Information Technology",
            "major": "Information Technology"
        }
    
    Input: 
    degree: Bachelor of Science in Occupational Therapy Assistant
    Output:
        {
            "name": "Bachelor of Science in Occupational Therapy Assistant",
            "major": "Occupational Therapy Assistant"
        }
    
    Input: 
    degree: Master of Computer Science
    Output:
        {
            "name": "Bachelor of Arts Major in Economics",
            "major": "N/A"
        }

    Extract the correct major for the following degree:
            ```
            $degree
            ```
"""

EDUCATION_LEVEL_PROMPT = """
    Education levels:
    [
        Primary Education,
        Secondary Education,
        High School Diploma,
        Vocational Education,
        Associate Degree,
        Bachelor’s Degree,
        Master’s Degree,
        Professional Degrees,
        Doctorate Degree,
        Post-Doctoral Programs
    ]
    
    Follow these instructions:
    1. Read the education levels.
    2. You were provided with a list of education levels. Based on the input degree provided below map the degree to one
     of the education levels following JSON format:
    {
        "name": Degree input, the same name you received in the input
        "education_level": The education level of the degree
    }
    
    Good output examples:
    Input: 
    degree: Associate of Applied Science in Information Technology
    Output:
        {
            "name": "Associate of Applied Science in Information Technology",
            "education_level": "Associate Degree"
        }
        
    Input: 
    degree: Bachelor of Science in Occupational Therapy Assistant
    Output:
        {
            "name": "Bachelor of Science in Occupational Therapy Assistant",
            "education_level": "Bachelor’s Degree"
        }
        
    Input: 
    degree: Master of Computer Science
    Output:
        {
            "name": "Master of Computer Science",
            "education_level": "Master's Degree"
        }
    
    Map the correct education level for the following degree:
            ```
            $degree
            ```
"""