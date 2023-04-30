import json
import os
import pickle
import socket
import sys
import timeit
from io import BytesIO

import avro
import fastavro
import msgpack
import xmltodict
import yaml
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
from dicttoxml import dicttoxml
from fastavro import writer

import ser_pb2

structure = dict(text='string', int=228, number=3.44, boolean=True, int_list=[1, 2, 3], dict={'key': 'value'})


def pickle_serialization():
    ser_time = timeit.timeit("pickle.dump(structure, open('output.dat', 'wb'))", number=10000, globals=globals())
    deser_time = timeit.timeit("pickle.load(open('output.dat', 'rb'))", number=10000, globals=globals())
    size = os.stat('output.dat').st_size
    return (ser_time, deser_time, size)


def xml_serialization():
    ser_time = timeit.timeit("xml_struct = dicttoxml(structure)", number=10000, globals=globals())
    size = dicttoxml(structure).__sizeof__()
    deser_time = timeit.timeit("xmltodict.parse(xml_struct)", setup="xml_struct = dicttoxml(structure)", number=10000,
                               globals=globals())
    return (ser_time, deser_time, size)


def json_serialization():
    ser_time = timeit.timeit("json_str = json.dumps(structure)", number=10000, globals=globals())
    size = json.dumps(structure).__sizeof__()
    deser_time = timeit.timeit("json.loads(json_str)", setup="json_str = json.dumps(structure)", number=10000,
                               globals=globals())
    return (ser_time, deser_time, size)


def get_struct():
    struct = ser_pb2.Structure()
    struct.string = structure["text"]
    struct.number = structure["int"]
    for num in structure["int_list"]:
        struct.array.append(num)
    struct.float_number = structure["number"]
    struct.bool = structure["boolean"]
    for key, value in structure["dict"].items():
        struct.dict[key] = value
    return struct


def protobuf_serialization():
    setup = "from __main__ import get_struct;" \
            "proto_struct = get_struct()"
    proto_struct = get_struct()
    ser_time = timeit.timeit("proto_struct.SerializeToString()", setup=setup, number=10000, globals=globals())
    size = proto_struct.SerializeToString().__sizeof__()
    deser_setup = "from __main__ import get_struct;" \
                  "proto_struct = get_struct();" \
                  "proto_ser = proto_struct.SerializeToString();" \
                  "deser_struct = ser_pb2.Structure()"
    deser_time = timeit.timeit("deser_struct.ParseFromString(proto_ser)", setup=deser_setup, number=10000,
                               globals=globals())
    return (ser_time, deser_time, size)

def serialize(schema, data): #вдохновлено https://habr.com/ru/articles/346698/
    bytes_writer = BytesIO()
    fastavro.schemaless_writer(bytes_writer, schema, data)
    return bytes_writer.getvalue()

def deserialize(schema, binary):
    bytes_writer = BytesIO()
    bytes_writer.write(binary)
    bytes_writer.seek(0)

    data = fastavro.schemaless_reader(bytes_writer, schema)
    return data

shema = {"name": "example.avro",
         "type": "record",
         "fields": [
             {"name": "text", "type": "string"},
             {"name": "int", "type": "int"},
             {"name": "number", "type": "float"},
             {"name": "boolean", "type": "boolean"},
             {"name": "int_list", "type": {"type": "array", "items": "int"}},
             {"name": "dict", "type": {"type": "map", "values": "string"}},
         ]
         }


def avro_serialization():
    setup = "from __main__ import serialize"
    ser_time = timeit.timeit("ser = serialize(shema, structure)", setup=setup, number=10000, globals=globals())
    size = serialize(shema, structure).__sizeof__()
    setup_deser = "from __main__ import serialize, deserialize;" \
                  "ser = serialize(shema, structure)"
    deser_time = timeit.timeit("deser = deserialize(shema, ser)", setup=setup_deser, number=10000,
                               globals=globals())
    return (ser_time, deser_time, size)

def yaml_serialization():
    ser_time = timeit.timeit("yaml.dump(structure)", number=10000, globals=globals())
    size = yaml.dump(structure).__sizeof__()
    setup_deser = "ser = yaml.dump(structure)"
    deser_time = timeit.timeit("yaml.load(ser, yaml.FullLoader)", setup=setup_deser, number=10000,
                               globals=globals())
    return (ser_time, deser_time, size)

def msg_pack_serialization():
    ser_time = timeit.timeit("msgpack.packb(structure)", number=10000, globals=globals())
    size = msgpack.packb(structure).__sizeof__()
    setup_deser = "ser = msgpack.packb(structure)"
    deser_time = timeit.timeit("msgpack.unpackb(ser)", setup=setup_deser, number=10000,
                               globals=globals())
    return (ser_time, deser_time, size)

def get_info():
    ser_time, deser_time, size = 0, 0, 0
    if (os.getenv('HOST') == 'PICKLE'):
        ser_time, deser_time, size = pickle_serialization()
    elif (os.getenv('HOST') == 'JSON'):
        ser_time, deser_time, size = json_serialization()
    elif (os.getenv('HOST') == 'XML'):
        ser_time, deser_time, size = xml_serialization()
    elif (os.getenv('HOST') == 'PROTOBUFF'):
        ser_time, deser_time, size = protobuf_serialization()
    elif (os.getenv('HOST') == 'AVRO'):
        ser_time, deser_time, size = avro_serialization()
    elif (os.getenv('HOST') == 'YAML'):
        ser_time, deser_time, size = yaml__serialization()
    elif (os.getenv('HOST') == 'MSGPACK'):
        ser_time, deser_time, size = msg_pack_serialization()
    data_to_send = os.getenv('HOST') + "-" + str(size) + "-" + str(int(ser_time * 1000)) + "ms" + "-" + str(
        int(deser_time * 1000)) + "ms"
    return data_to_send

if __name__ == "__main__":
    host = os.environ['HOST']
    port = int(os.environ['PORT'])
    print(host, port)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as socket1:
        socket1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        socket1.bind(('', port))
        while True:
            print("in while")
            _, address = socket1.recvfrom(1024)
            print("after recv")
            data = get_info()
            print(data)
            socket1.sendto(bytes(data + "\n", "utf-8"), address)
