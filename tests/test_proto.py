import unittest
import numpy as np
from tensorflow.core.framework import tensor_pb2, tensor_shape_pb2, types_pb2
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api.proto import dtypes_as_dtype, make_tensor_proto, np_to_protobuf


class TestTensorConversion(unittest.TestCase):
    def test_dtypes_as_dtype(self):
        self.assertEqual(dtypes_as_dtype("float32"), types_pb2.DT_FLOAT)
        with self.assertRaises(Exception):
            dtypes_as_dtype("int32")

    def test_make_tensor_proto(self):
        data = np.array([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)
        tensor_proto = make_tensor_proto(data)

        # Add your assertions based on the expected values
        self.assertEqual(tensor_proto.dtype, types_pb2.DT_FLOAT)
        self.assertEqual(len(tensor_proto.tensor_shape.dim), 2)
        # Add more assertions as needed

    def test_np_to_protobuf(self):
        data = np.array([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)
        tensor_proto = np_to_protobuf(data)

        # Add your assertions based on the expected values
        self.assertEqual(tensor_proto.dtype, types_pb2.DT_FLOAT)
        self.assertEqual(len(tensor_proto.tensor_shape.dim), 2)
        # Add more assertions as needed


if __name__ == "__main__":
    unittest.main()
