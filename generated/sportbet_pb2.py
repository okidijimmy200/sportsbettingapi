# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sportbet.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0esportbet.proto\"\xa6\x01\n\x10\x43reateBetRequest\x12\x0e\n\x06league\x18\x01 \x01(\t\x12\x11\n\thome_team\x18\x02 \x01(\t\x12\x11\n\taway_team\x18\x03 \x01(\t\x12\x1a\n\x12home_team_win_odds\x18\x04 \x01(\x02\x12\x1a\n\x12\x61way_team_win_odds\x18\x05 \x01(\x02\x12\x11\n\tdraw_odds\x18\x06 \x01(\x02\x12\x11\n\tgame_date\x18\x07 \x01(\t\"1\n\x11\x43reateBetResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0e\n\x06reason\x18\x02 \x01(\t\"F\n\x0eReadBetRequest\x12\x0e\n\x06league\x18\x01 \x01(\t\x12\x12\n\nstart_date\x18\x02 \x01(\t\x12\x10\n\x08\x65nd_date\x18\x03 \x01(\t\"\xa6\x01\n\x04Odds\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06league\x18\x02 \x01(\t\x12\x11\n\thome_team\x18\x03 \x01(\t\x12\x11\n\taway_team\x18\x04 \x01(\t\x12\x1a\n\x12home_team_win_odds\x18\x05 \x01(\x02\x12\x1a\n\x12\x61way_team_win_odds\x18\x06 \x01(\x02\x12\x11\n\tdraw_odds\x18\x07 \x01(\x02\x12\x11\n\tgame_date\x18\x08 \x01(\t\"H\n\x0fReadBetResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x17\n\x08response\x18\x02 \x03(\x0b\x32\x05.Odds\x12\x0e\n\x06reason\x18\x03 \x01(\t\"\xa6\x01\n\x10UpdateBetRequest\x12\x0e\n\x06league\x18\x01 \x01(\t\x12\x11\n\thome_team\x18\x02 \x01(\t\x12\x11\n\taway_team\x18\x03 \x01(\t\x12\x1a\n\x12home_team_win_odds\x18\x04 \x01(\x02\x12\x1a\n\x12\x61way_team_win_odds\x18\x05 \x01(\x02\x12\x11\n\tdraw_odds\x18\x06 \x01(\x02\x12\x11\n\tgame_date\x18\x07 \x01(\t\"1\n\x11UpdateBetResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0e\n\x06reason\x18\x02 \x01(\t\"[\n\x10\x44\x65leteBetRequest\x12\x0e\n\x06league\x18\x01 \x01(\t\x12\x11\n\thome_team\x18\x02 \x01(\t\x12\x11\n\taway_team\x18\x03 \x01(\t\x12\x11\n\tgame_date\x18\x04 \x01(\t\"1\n\x11\x44\x65leteBetResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0e\n\x06reason\x18\x02 \x01(\t2\xe5\x01\n\x19SportBetManagementService\x12\x32\n\tCreateBet\x12\x11.CreateBetRequest\x1a\x12.CreateBetResponse\x12,\n\x07ReadBet\x12\x0f.ReadBetRequest\x1a\x10.ReadBetResponse\x12\x32\n\tUpdateBet\x12\x11.UpdateBetRequest\x1a\x12.UpdateBetResponse\x12\x32\n\tDeleteBet\x12\x11.DeleteBetRequest\x1a\x12.DeleteBetResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sportbet_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CREATEBETREQUEST._serialized_start=19
  _CREATEBETREQUEST._serialized_end=185
  _CREATEBETRESPONSE._serialized_start=187
  _CREATEBETRESPONSE._serialized_end=236
  _READBETREQUEST._serialized_start=238
  _READBETREQUEST._serialized_end=308
  _ODDS._serialized_start=311
  _ODDS._serialized_end=477
  _READBETRESPONSE._serialized_start=479
  _READBETRESPONSE._serialized_end=551
  _UPDATEBETREQUEST._serialized_start=554
  _UPDATEBETREQUEST._serialized_end=720
  _UPDATEBETRESPONSE._serialized_start=722
  _UPDATEBETRESPONSE._serialized_end=771
  _DELETEBETREQUEST._serialized_start=773
  _DELETEBETREQUEST._serialized_end=864
  _DELETEBETRESPONSE._serialized_start=866
  _DELETEBETRESPONSE._serialized_end=915
  _SPORTBETMANAGEMENTSERVICE._serialized_start=918
  _SPORTBETMANAGEMENTSERVICE._serialized_end=1147
# @@protoc_insertion_point(module_scope)
