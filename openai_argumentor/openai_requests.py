import json
import pandas as pd
from string import Template
from retrain_openai.models.ext_models import CompletionResponse
from retrain_openai.openai import openai
from retrain_logger.logger import logger_setup
from openai_argumentor.openai_prompts import ALTERNATIVE_AND_ACRONYMS_PROMPT, EDUCATION_FIELD_PROMPT, MAJOR_PROMPT

logger = logger_setup(__name__)


def _send_completion_request(
        model: str,
        max_tokens: int,
        temperature: float,
        prompt: list
) -> CompletionResponse:
    """
    Sends requests to openai
    Args:
        model: GPT model
        max_tokens: for model
        temperature: for model
        prompt: for model request

    Returns: response to request from openai
    """
    logger.info(f"Request from open ai\n"
                f"model: {model}\n"
                f"max_tokens: {max_tokens}\n"
                f"temperature: {temperature}\n"
                f"prompt: {prompt}")
    try:
        response = openai.ChatCompletion.create(
            model=model, max_tokens=max_tokens, temperature=temperature, messages=prompt
        )
    except Exception as e:
        logger.error(f"Process failed for this prompt: {prompt}")
        logger.error(e)
        raise e
    else:
        return response


def parse_openai_response(response):
    """
    Parsing the result from open.ai argumentor
    Args:
        response: response from open.ai
    Returns:
        The content of the response
    """
    try:
        content = response[0]['result'][0]['content']
        if 'Output' in content:
            content = content.replace("Output", "").strip(":")
    except KeyError:
        logger.info(f"Content not found for the response: {response}")
        logger.error(f"Content not found for the response: {response}")
        return '-1'
    else:
        return content


def generate_alternative_and_acronyms(
        data: list
):
    num_degrees = len(data)
    alt_acronyms = []
    logger.info(f"Generating alternative names and acronyms for [{num_degrees}] degrees")
    for i, degree in enumerate(data):
        logger.info(f"Generating response for '{degree}' [{i}/{num_degrees}] degree")
        prompt_template = Template(ALTERNATIVE_AND_ACRONYMS_PROMPT)
        final_prompt = prompt_template.substitute(
            **{"degree": degree})
        logger.info(f"Prompt: {final_prompt}")
        logger.info(f"[{i}/{num_degrees}] alt degree and acronym prompt: {final_prompt}")
        message = [{"role": "user", "content": final_prompt}]
        result = _send_completion_request("gpt-35-turbo-16k", 1000, 0.8, message)
        logger.info(f"Result from openai: {result}")
        parsed_result = parse_openai_response(result)
        if parsed_result == '-1':
            continue
        parsed_result = json.loads(parse_openai_response(result))
        parsed_result['input'] = degree
        alt_acronyms.append(parsed_result)
    alt_acronyms_df = pd.DataFrame(alt_acronyms)
    return alt_acronyms_df


def generate_education_fields(
        data: pd.DataFrame
) -> pd.DataFrame:
    if data.empty:
        return pd.DataFrame()
    total = len(data)
    education_fields = []

    for index, row in data.iterrows():
        logger.info(f"Generating education_field for [{index}/{total}] degrees")
        logger.info(f"prompt for degree: {row['name']}")
        final_prompt = Template(EDUCATION_FIELD_PROMPT)
        final_prompt = final_prompt.substitute(**{"degree": row['name']})
        logger.info(f"Prompt: {final_prompt}")
        message = [{"role": "user", "content": final_prompt}]
        logger.info(f"[{index}/{total}] education fields prompt: {message}")
        result = _send_completion_request("gpt-35-turbo", 1000, 0.8, message)
        logger.info(f"Result from openai: {result}")
        parsed_result = parse_openai_response(result)
        if parsed_result == '-1':
            continue
        parsed_result = json.loads(parsed_result)
        education_fields.append(parsed_result)
    education_fields_df = pd.DataFrame(education_fields)
    return education_fields_df


def generate_major(
        data: pd.DataFrame
) -> pd.DataFrame:
    if data.empty:
        return pd.DataFrame()
    total = len(data)
    major = []

    for index, row in data.iterrows():
        logger.info(f"Generating major for [{index}/{total}] degrees")
        logger.info(f"prompt for degree: {row['name']}")
        final_prompt = Template(MAJOR_PROMPT)
        final_prompt = final_prompt.substitute(**{"degree": row['name']})
        logger.info(f"Prompt: {final_prompt}")
        message = [{"role": "user", "content": final_prompt}]
        logger.info(f"[{index}/{total}] major degree prompt: {message}")
        result = _send_completion_request("gpt-35-turbo", 1000, 0.8, message)
        logger.info(f"Result from openai: {result}")
        parsed_result = parse_openai_response(result)
        if parsed_result == '-1':
            continue
        parsed_result = json.loads(parse_openai_response(result))
        major.append(parsed_result)
    major_df = pd.DataFrame(major)
    return major_df


def generate_education_level(data: list):
    pass
