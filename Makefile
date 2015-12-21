.PHONY: proto

proto:
	protoc --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` knowledge.proto
	cp knowledge_pb2.py tests/knowledge_pb2.py