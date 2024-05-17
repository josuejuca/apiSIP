from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

from pydantic import BaseModel

Base = declarative_base()
Apagar = declarative_base()
class Extension(Base):
    __tablename__ = 'v_extensions'

    extension_uuid = Column(String, primary_key=True) # ID do usuario 
        
    domain_uuid = Column(String) # ID do dominio 
    extension = Column(String) # usuario
    number_alias = Column(String) 
    password = Column(String) # Senha do usuario
    accountcode = Column(String) # Dominio (  ex: sip.josuejuca.com )
    effective_caller_id_name = Column(String) 
    effective_caller_id_number = Column(String)
    outbound_caller_id_name = Column(String)
    outbound_caller_id_number = Column(String)
    emergency_caller_id_name = Column(String)
    emergency_caller_id_number = Column(String)
    directory_first_name = Column(String)
    directory_last_name = Column(String)
    directory_visible = Column(String) # True / False
    directory_exten_visible = Column(String) # True / False
    max_registrations = Column(String) 
    limit_max = Column(String) # 5 ( padrao )
    limit_destination = Column(String)  # !USER_BUSY 
    missed_call_app = Column(String)  
    missed_call_data = Column(String)
    user_context = Column(String) # Dominio (  ex: sip.josuejuca.com )
    toll_allow = Column(String)
    call_timeout = Column(String) # 30
    call_group = Column(String)
    call_screen_enabled = Column(String) # True / False ( Padrao falso )
    user_record = Column(String)
    hold_music = Column(String)
    auth_acl = Column(String)
    cidr = Column(String)
    sip_force_contact = Column(String)
    nibble_account = Column(String)
    sip_force_expires = Column(String)
    mwi_account = Column(String)
    sip_bypass_media = Column(String)
    unique_id = Column(String)
    dial_string = Column(String)
    dial_user = Column(String)
    dial_domain = Column(String)
    do_not_disturb = Column(String)
    forward_all_destination = Column(String)
    forward_all_enabled = Column(String)
    forward_busy_destination = Column(String)
    forward_busy_enabled = Column(String)
    forward_no_answer_destination = Column(String)
    forward_no_answer_enabled = Column(String)
    forward_user_not_registered_destination = Column(String)
    forward_user_not_registered_enabled = Column(String)
    follow_me_uuid = Column(String)
    follow_me_enabled = Column(String)
    follow_me_destinations = Column(String)
    extension_language = Column(String)
    extension_dialect = Column(String) # US 
    extension_voice = Column(String) # Callie
    extension_type = Column(String) #default 
    enabled = Column(String) # true
    description = Column(String)
    absolute_codec_string = Column(String)
    force_ping = Column(String)
    insert_date = Column(String)  # data de criação 2024-05-12 00:38:38.510298-03
    insert_user = Column(String) # ID do usuario ( 30c32664-b257-4be4-90cd-b4150e16cf33 )
    update_date = Column(String)
    update_user = Column(String)


class ApagarExtension(Apagar):
    __tablename__ = 'v_extensions'

    extension_uuid = Column(String, primary_key=True) # ID do usuario 
        
        
        

class ExtensionCreate(BaseModel):

    extension_uuid: str
        
    domain_uuid: str
    extension: str
    number_alias: str
    password: str
    accountcode: str
    effective_caller_id_name: str
    effective_caller_id_number: str
    outbound_caller_id_name: str
    outbound_caller_id_number: str
    emergency_caller_id_name: str
    emergency_caller_id_number: str
    directory_first_name: str
    directory_last_name: str
    directory_visible: str
    directory_exten_visible: str
    max_registrations: str
    limit_max: str
    limit_destination: str
    missed_call_app: str
    missed_call_data: str
    user_context: str
    toll_allow: str
    call_timeout: str
    call_group: str
    call_screen_enabled: str
    user_record: str
    hold_music: str
    auth_acl: str
    cidr: str
    sip_force_contact: str
    nibble_account: str
    sip_force_expires: str
    mwi_account: str
    sip_bypass_media: str
    unique_id: str
    dial_string: str
    dial_user: str
    dial_domain: str
    do_not_disturb: str
    forward_all_destination: str
    forward_all_enabled: str
    forward_busy_destination: str
    forward_busy_enabled: str
    forward_no_answer_destination: str
    forward_no_answer_enabled: str
    forward_user_not_registered_destination: str
    forward_user_not_registered_enabled: str
    follow_me_uuid: str
    follow_me_enabled: str
    follow_me_destinations: str
    extension_language: str
    extension_dialect: str
    extension_voice: str
    extension_type: str
    enabled: str
    description: str
    absolute_codec_string: str
    force_ping: str
    insert_date: str
    insert_user: str
    update_date: str
    update_user: str
        
