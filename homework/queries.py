def mapper_query_4(sequence):
    """Mapper"""
    result = []
    for index, (_, row) in enumerate(sequence):
        if index == 0:
            continue  # saltamos header
        else:
            row_values = row.strip().split(",")
            total_bill = float(row_values[0])
            tip = float(row_values[1])
            day = row_values[3]
            tip_rate = tip / total_bill
            result.append((day, tip_rate))
    return result


def reducer_query_4(sequence):
    """Reducer"""
    from collections import defaultdict
    grouped = defaultdict(list)
    for key, value in sequence:
        grouped[key].append(value)
    result = []
    for key, values in grouped.items():
        avg_val = sum(values) / len(values)
        result.append((key, avg_val))
    return result


def mapper_query_5(sequence):
    """Mapper"""
    result = []
    for index, (_, row) in enumerate(sequence):
        if index == 0:
            continue
        else:
            row_values = row.strip().split(",")
            sex = row_values[2]
            result.append((sex, 1))
    return result


def reducer_query_5(sequence):
    """Reducer"""
    from collections import defaultdict
    counts = defaultdict(int)
    for key, value in sequence:
        counts[key] += value
    return list(counts.items())


def mapper_query_6(sequence):
    """Mapper"""
    result = []
    for index, (_, row) in enumerate(sequence):
        if index == 0:
            continue
        else:
            row_values = row.strip().split(",")
            smoker = row_values[3] if len(row_values) > 3 else None
            total_bill = float(row_values[0])
            result.append((smoker, total_bill))
    return result


def reducer_query_6(sequence):
    """Reducer"""
    from collections import defaultdict
    totals = defaultdict(float)
    for key, value in sequence:
        totals[key] += value
    return list(totals.items())


def run():
    """Orquestador"""

    queries = {
        "query_1": (mapper_query_1, reducer_query_1),
        "query_2": (mapper_query_2, reducer_query_2),
        "query_3": (mapper_query_3, reducer_query_3),
        "query_4": (mapper_query_4, reducer_query_4),
        "query_5": (mapper_query_5, reducer_query_5),
        "query_6": (mapper_query_6, reducer_query_6),
    }

    for qname, (mapper, reducer) in queries.items():
        path = f"files/{qname}"
        if os.path.exists(path):
            shutil.rmtree(path)

        mapreduce(
            input_folder="files/input/",
            output_folder=path,
            mapper_fn=mapper,
            reducer_fn=reducer,
        )


if __name__ == "__main__":
    run()
