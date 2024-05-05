ALTERNATIVE_AND_ACRONYMS_PROMPT = """
    Given an input representing a degree, extract the following fields - name, acronyms, alternative_names and 
    alternative_acronyms. 
    
    Follow these instructions:
    1. Don't add any alternative names if they don't appear in the input degree.
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

    Based on the input degree provided below create an extraction in the following JSON format:
    {
        "name": Degree input, the same name you received in the input
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
    1. If there isn't any major mark ''.
    
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
            "education_field": "N/A"
        }

    Extract the correct major for the following degree:
            ```
            $degree
            ```
"""

EDUCATION_LEVEL_PROMPT = """
    
"""


MAJOR_PROMPT1 = """
    Given an input representing a degree please extract the major following these instructions:
    1. If there isn't any major mark ''.
    
    You will receive an input, delimited by triple quotes, in a JSON list formatting - input example:
    ["Master of Computer Science", "Bachelor of Arts in Economics", "Bachelor of Science in Occupational Therapy 
    Assistant"...]
    You should output a JSON list containing the new formatted title in the same order as the input - output
    example: ["N/A", "Economics", "Occupational Therapy Assistant" ...]
    
    Extract the correct major for the following degrees:
            ```
            $degrees
            ```
"""


EDUCATION_FIELD_PROMPT1 = """
    Given an input representing a degree please extract the education field.

    You will receive an input, delimited by triple quotes, in a JSON list formatting - input example:
    ["Master of Computer Science", "Bachelor of Arts in Economics", "Bachelor of Science in Occupational 
    Therapy Assistant"...]
    You should output a JSON list containing the new formatted title in the same order as the input - output
    example: ["Computer Science", "Liberal Arts", "Science" ...]

    Extract the correct education field for the following degrees:
            ```
            $degrees
            ```
"""
