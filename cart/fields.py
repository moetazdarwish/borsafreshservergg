STATUS = [
    #### Product
    ('CREATED', 'CREATED'),
    ('PAID', 'PAID'),
    ('ACCEPT', 'ACCEPT'),
    ('REJECT', 'REJECT'),
    ('COLLECTION POINT', 'COLLECTION POINT'),
    ('RECEIVED', 'RECEIVED'),
    ('PROCESSING', 'PROCESSING'),
    ('ITEMS DELIVERY OUT', 'ITEMS DELIVERY OUT'),

    ### point
    ('COLLECTION POINT', 'COLLECTION POINT'),
    ('READY TO DELIVERY', 'READY TO DELIVERY'),
    ('SHIPPED', 'SHIPPED'),

    ######order
    ('CANCELLED', 'CANCELLED'),
    ('REFUND', 'REFUND'),
    ('REJECT', 'REJECT'),
    ('RETURN', 'RETURN'),
    ###### delivery
    ('DELIVERY OUT', 'DELIVERY OUT'),
    ('DELIVERED', 'DELIVERED'),
    ('UNABLE TO DELIVERY', 'UNABLE TO DELIVERY'),

    ####
    ('PICK UP', 'PICK UP'),
    ('CONFIRMED', 'CONFIRMED'),
    ('COLLECTED', 'COLLECTED'),
    ('RECEIVED', 'RECEIVED'),
    ####
    ('TRANSFERED', 'TRANSFERED'),
    ('FIXED', 'FIXED'),
    ('RATE', 'RATE'),
    #####
    ('CPC', 'CPC'),
    ('DATE', 'DATE'),
    ('SPONSOR', 'SPONSOR'),
    ('ADPAID', 'ADPAID'),
    ##
    ('PENDING', 'PENDING'),
    ('UNEARNED REVENUE', 'UNEARNED REVENUE'),
    ####
    ('OFFER', 'OFFER'),
    ('EXECUTED', 'EXECUTED'),
    ('MARKET', 'MARKET'),
    ('OFFER REMOVED', 'OFFER REMOVED'),
    ('LOST SELL', 'LOST SELL'),
]
SUBSTATUS = [
    #### OrderProduct
    ('CREATED', 'CREATED'),
    ('CONFIRMED', 'CONFIRMED'),
    ('ACCEPT', 'ACCEPT'),
    ('REJECT', 'REJECT'),
    ('DELIVERY OUT', 'DELIVERY OUT'),
    ('DELIVERED', 'DELIVERED'),
    ('RESCHEDULE', 'RESCHEDULE'),
    ('REFUSED', 'REFUSED'),
    ('CANCELLED', 'CANCELLED'),
]
SCALE = [
    'KG',
    'POUNDS ',
    'BUNCH',
]
FAILED = [
    ('ABSENT', 'ABSENT'),
    ('INCORRECT ADDRESS', 'INCORRECT ADDRESS'),
]
FAQFEILD = [
    ('GENERAL', 'GENERAL'),
    ('DELIVERY', 'DELIVERY'),
    ('RETURN', 'RETURN'),
    ('GROWING', 'GROWING'),
    ('PRIVACY', 'PRIVACY'),
    ('TRADER', 'TRADER'),
    ('TRPOLICY', 'TRPOLICY'),
]
