ServicesNameMap = {
    'MaDirect_local': 1,
    'MaDirect_dev': 2,
    'MaDirect_test': 3,
    'MaDirect_stage': 4,
    'MaDirect_prod': 5,
    'MaDirect_pre': 6,
}

NOTHING = 'nothing'
UNKNOWN = 'unknown'

EventTypeMap = {
    UNKNOWN: 0,
    NOTHING: 1,
    'create': 2,
    'update': 3,
    'delete': 4,
    'loaded': 5,
    'accepted': 6,
    'decline_processed_report': 7,
    'accept_processed_report': 8,
    'accept_processed_report_element': 9,
    'decline_worker_report': 10,
    'accept_worker_report': 11,
    'load_worker_report': 12,
    'soft_delete': 13,
    'partner_status_decline_processed_report': 14,
    'partner_status_accept_processed_report': 15,
}
