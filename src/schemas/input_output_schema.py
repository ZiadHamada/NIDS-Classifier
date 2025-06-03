from pydantic import BaseModel
from typing import List, Union

class ClassifierRequest(BaseModel):
      L4_SRC_PORT: int
      L4_DST_PORT: int
      L7_PROTO: float
      IN_BYTES: int
      DURATION_OUT: int
      MIN_TTL: int
      MAX_TTL: int
      LONGEST_FLOW_PKT: int
      SRC_TO_DST_AVG_THROUGHPUT: int
      ICMP_IPV4_TYPE: int
      DNS_QUERY_TYPE: int
      
      
class ClassifierResponse(BaseModel):
    label: Union[str, int]  # or whatever type your model predicts
    confidence: List[float]  # or Union[List[float], List[List[float]]
