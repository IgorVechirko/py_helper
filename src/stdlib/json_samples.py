import os
import json
import res


def deserialize_json():
    file_path = os.path.join(res.res_path(), "goods.json")

    with open(file_path, "r") as file:
        file_ctx = json.load(file)
        print(file_ctx, "\n")

        file.seek(0)
        json_str = ""
        line = file.readline()
        while len(line):
            json_str = json_str + line.strip()
            line = file.readline()

        print(json.loads(json_str))


def serialize_json():
    all_path = os.path.join(res.res_path(), "goods.json")
    cheap_path = goods_path = os.path.join(res.res_path(), "cheap_goods.json")

    os.remove(cheap_path)

    with open(all_path, 'r') as all_file:
        with open(cheap_path, "w") as cheap_file:
            json_obj = json.load(all_file)

            cheap_goods = []
            for good in json_obj["goods"]:
                if int(good['price']) < 10:
                    cheap_goods.append(good)

            output_json_obj = {"goods": cheap_goods}
            json.dump(output_json_obj, cheap_file, indent=2)

            print(json.dumps(output_json_obj, indent=2))


serialize_json()