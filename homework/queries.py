"""Taller evaluable"""

# pylint: disable=broad-exception-raised
# pylint: disable=import-error

from homework.mapreduce import mapreduce  # type: ignore

#
# Columns:
# total_bill, tip, sex, smoker, day, time, size
#

#
# QUERY 1:
# SELECT *, tip/total_bill as tip_rate
# FROM tips;
#

def mapper_query_1(sequence):
    """Mapper"""
    result = []
    for index, (_, row) in enumerate(sequence):
        if index == 0:
            result.append(
                (index, row.strip() + ",tip_rate")
            )
        else:
            row_values = row.strip().split(",")
            total_bill = float(row_values[0])
            tip = float(row_values[1])
            tip_rate = tip / total_bill
            result.append((index, row.strip() + "," + str(tip_rate)))
    return result


def reducer_query_1(sequence):
    """Reducer"""
    return sequence


#
# ORQUESTADOR:
#
def run():
    """Orquestador"""

    mapreduce(
        input_folder="files/input/", 
        output_folder="files/query_1", 
        mapper_fn=mapper_query_1, 
        reducer_fn=reducer_query_1,
    )


if __name__ == "__main__":

    run()
"""Taller evaluable"""

# pylint: disable=broad-exception-raised
# pylint: disable=import-error

from homework.mapreduce import mapreduce  # type: ignore
import shutil
import os
#
# Columns:
# total_bill, tip, sex, smoker, day, time, size
#

#
# QUERY 1:
# SELECT *, tip/total_bill as tip_rate
# FROM tips;
#

def mapper_query_1(sequence):
    """Mapper"""
    result = []
    for index, (_, row) in enumerate(sequence):
        if index == 0:
            result.append(
                (index, row.strip() + ",tip_rate")
            )
        else:
            row_values = row.strip().split(",")
            total_bill = float(row_values[0])
            tip = float(row_values[1])
            tip_rate = tip / total_bill
            result.append((index, row.strip() + "," + str(tip_rate)))
    return result


def reducer_query_1(sequence):
    """Reducer"""
    return sequence


#
# SELECT *
# FROM tips
# WHERE time = 'Dinner';
#
def mapper_query_2(sequence):
    """Mapper"""
    result = []
    for index, (_, row) in enumerate(sequence):
        if index == 0:
            result.append((index, row.strip()))
        else:
            row_values = row.strip().split(",")
            if row_values[5] == "Dinner":
                result.append((index, row.strip()))
    return result


def reducer_query_2(sequence):
    """Reducer"""
    return sequence

#
# SELECT *
# FROM tips
# WHERE time = 'Dinner' AND tip > 5.00;
#
def mapper_query_3(sequence):
    """Mapper"""
    result = []
    for index, (_, row) in enumerate(sequence):
        if index == 0:
            result.append((index, row.strip()))
        else:
            row_values = row.strip().split(",")
            if row_values[5] == "Dinner" and float(row_values[1]) > 5.00:
                result.append((index, row.strip()))
    return result


def reducer_query_3(sequence):
    """Reducer"""
    return sequence



#
# SELECT *
# FROM tips
# WHERE size >= 5 OR total_bill > 45;
#
def mapper_query_4(sequence):
    """Mapper"""
    result = []
    for index, (_, row) in enumerate(sequence):
        if index == 0:
            result.append((index, row.strip()))
        else:
            row_values = row.strip().split(",")
            if int(row_values[6]) >= 5 or float(row_values[0]) > 45:
                result.append((index, row.strip()))
    return result


def reducer_query_4(sequence):
    """Reducer"""
    return sequence



#
# SELECT sex, count(*)
# FROM tips
# GROUP BY sex;
#
def mapper_query_5(sequence):
    """Mapper"""
    result = []
    for index, (_, row) in enumerate(sequence):
        if index == 0:
            continue
        row_values = row.strip().split(",")
        result.append((row_values[2], 1))
    return result


def reducer_query_5(sequence):
    """Reducer"""
    counter = dict()
    for key, value in sequence:
        if key not in counter:
            counter[key] = 0
        counter[key] += value
    return list(counter.items())



#
# ORQUESTADOR:
#
def run():
    """Orquestador"""

    if os.path.exists("files/query_1"):
            shutil.rmtree("files/query_1")

    mapreduce(
        input_folder="files/input/", 
        output_folder="files/query_1", 
        mapper_fn=mapper_query_1, 
        reducer_fn=reducer_query_1,
    )


    if os.path.exists("files/query_2"):
        shutil.rmtree("files/query_2")

    mapreduce(
        input_folder="files/input/", 
        output_folder="files/query_2", 
        mapper_fn=mapper_query_2, 
        reducer_fn=reducer_query_2,
    )    

    if os.path.exists("files/query_3"):
        shutil.rmtree("files/query_3")

    mapreduce(
        input_folder="files/input/", 
        output_folder="files/query_3", 
        mapper_fn=mapper_query_3, 
        reducer_fn=reducer_query_3,
    )    


    if os.path.exists("files/query_4"):
        shutil.rmtree("files/query_4")

    mapreduce(
        input_folder="files/input/", 
        output_folder="files/query_4", 
        mapper_fn=mapper_query_4, 
        reducer_fn=reducer_query_4,
    )    

    if os.path.exists("files/query_5"):
        shutil.rmtree("files/query_5")

    mapreduce(
        input_folder="files/input/", 
        output_folder="files/query_5", 
        mapper_fn=mapper_query_5, 
        reducer_fn=reducer_query_5,
    )    

if __name__ == "__main__":
  run()
