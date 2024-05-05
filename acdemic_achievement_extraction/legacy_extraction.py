import json
import uuid


def parse_raw_academic_achievements(
        input_data: list,
        file_path: str
):
    json_data = []
    for item in input_data:
        main_item = item
        alternative = []
        for i, deg in enumerate(item.split('/')):
            print("main:", main_item)
            alternative.append(main_item)
            if i == 0:
                alt = deg.strip(')')
                a = alt.find('(')
                alternative.append(alt[a + 1:])
            else:
                if ")" in deg and "(" not in deg:
                    alternative.append(deg.strip(')'))
                else:
                    alternative.append(deg)
                print("deg:", deg)
                alt = deg.strip(')')
                a = alt.find('(')
                if len(deg) != len(alt[a + 1:]):
                    alternative.append(alt[a + 1:])
            alternative = list(set(alternative))

            json_file = {"degree": alt[a + 1:], "uuid": str(uuid.uuid4())}
            json_data.append(json_file)

    with open(f"{file_path}.json", "w") as json_file:
        json.dump(json_data, json_file, indent=4)
