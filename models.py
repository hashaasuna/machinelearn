# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Coupenlog(models.Model):
    coupenid = models.BigIntegerField(db_column='CoupenID', blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='BarCode', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    enabled = models.CharField(db_column='Enabled', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    begindate = models.CharField(db_column='BeginDate', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    enddate = models.CharField(db_column='EndDate', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    disamount = models.CharField(db_column='DisAmount', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dispercent = models.CharField(db_column='DisPercent', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descr = models.CharField(db_column='Descr', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    invtid = models.CharField(db_column='InvtID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rowstatus = models.CharField(db_column='RowStatus', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CoupenLog'


class Deleteditem(models.Model):
    deleteditemid = models.BigIntegerField(db_column='DeletedItemID', primary_key=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    deleteddate = models.CharField(db_column='DeletedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    deletedtimestamp = models.BigIntegerField(db_column='DeletedTimeStamp')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'DeletedItem'


class Mdata(models.Model):
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    month = models.IntegerField(db_column='Month', blank=True, null=True)  # Field name made lowercase.
    day = models.IntegerField(db_column='Day', blank=True, null=True)  # Field name made lowercase.
    daynumofweek = models.IntegerField(db_column='DayNumOfWeek', blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    invtid = models.CharField(db_column='InvtID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salesprice = models.DecimalField(db_column='SalesPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MData'


class MspeerConflictdetectionconfigrequest(models.Model):
    publication = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    sent_date = models.DateTimeField()
    timeout = models.IntegerField()
    modified_date = models.DateTimeField()
    progress_phase = models.CharField(max_length=32, db_collation='SQL_Latin1_General_CP1_CI_AS')
    phase_timed_out = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'MSpeer_conflictdetectionconfigrequest'


class MspeerConflictdetectionconfigresponse(models.Model):
    request_id = models.IntegerField()
    peer_node = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    peer_db = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    peer_version = models.IntegerField(blank=True, null=True)
    peer_db_version = models.IntegerField(blank=True, null=True)
    is_peer = models.BooleanField(blank=True, null=True)
    conflictdetection_enabled = models.BooleanField(blank=True, null=True)
    originator_id = models.IntegerField(blank=True, null=True)
    peer_conflict_retention = models.IntegerField(blank=True, null=True)
    peer_continue_onconflict = models.BooleanField(blank=True, null=True)
    peer_subscriptions = models.TextField(blank=True, null=True)  # This field type is a guess.
    progress_phase = models.CharField(max_length=32, db_collation='SQL_Latin1_General_CP1_CI_AS')
    modified_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSpeer_conflictdetectionconfigresponse'
        unique_together = (('request_id', 'peer_node', 'peer_db'),)


class MspeerLsns(models.Model):
    last_updated = models.DateTimeField(blank=True, null=True)
    originator = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    originator_db = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    originator_publication = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    originator_publication_id = models.IntegerField(blank=True, null=True)
    originator_db_version = models.IntegerField(blank=True, null=True)
    originator_lsn = models.BinaryField(blank=True, null=True)
    originator_version = models.IntegerField(blank=True, null=True)
    originator_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSpeer_lsns'
        unique_together = (('originator', 'originator_db', 'originator_publication_id', 'originator_db_version', 'originator_lsn'),)


class MspeerOriginatoridHistory(models.Model):
    originator_publication = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    originator_id = models.IntegerField()
    originator_node = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    originator_db = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    originator_db_version = models.IntegerField()
    originator_version = models.IntegerField()
    inserted_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'MSpeer_originatorid_history'
        unique_together = (('originator_publication', 'originator_id', 'originator_node', 'originator_db', 'originator_db_version'),)


class MspeerRequest(models.Model):
    id = models.AutoField()
    publication = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    sent_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=4000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSpeer_request'


class MspeerResponse(models.Model):
    request_id = models.IntegerField(blank=True, null=True)
    peer = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    peer_db = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    received_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSpeer_response'


class MspeerTopologyrequest(models.Model):
    id = models.AutoField()
    publication = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    sent_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSpeer_topologyrequest'


class MspeerTopologyresponse(models.Model):
    request_id = models.IntegerField(blank=True, null=True)
    peer = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    peer_version = models.IntegerField(blank=True, null=True)
    peer_db = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    originator_id = models.IntegerField(blank=True, null=True)
    peer_conflict_retention = models.IntegerField(blank=True, null=True)
    received_date = models.DateTimeField(blank=True, null=True)
    connection_info = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'MSpeer_topologyresponse'


class MspubIdentityRange(models.Model):
    objid = models.IntegerField(unique=True)
    range = models.BigIntegerField()
    pub_range = models.BigIntegerField()
    current_pub_range = models.BigIntegerField()
    threshold = models.IntegerField()
    last_seed = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSpub_identity_range'


class Mytmp(models.Model):
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    autoposting = models.CharField(db_column='AutoPosting', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rowstatus = models.CharField(db_column='RowStatus', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MyTmp'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    email = models.CharField(max_length=254, db_collation='SQL_Latin1_General_CP1_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Clterminalconfig(models.Model):
    terminalid = models.CharField(db_column='TerminalID', primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastbatchno = models.CharField(db_column='LastBatchNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lasttraceno = models.IntegerField(db_column='LastTraceNo')  # Field name made lowercase.
    issettlemented = models.CharField(db_column='IsSettlemented', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'clTerminalConfig'


class Clterminaltxn(models.Model):
    loyaltyrefno = models.CharField(db_column='LoyaltyRefNo', primary_key=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txndate = models.CharField(db_column='TxnDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txncode = models.CharField(db_column='TxnCode', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cardid = models.CharField(db_column='CardID', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cardholder = models.CharField(db_column='CardHolder', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cardexpirydate = models.CharField(db_column='CardExpiryDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    batchno = models.IntegerField(db_column='BatchNo')  # Field name made lowercase.
    traceno = models.IntegerField(db_column='TraceNo')  # Field name made lowercase.
    merchantid = models.CharField(db_column='MerchantID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    terminalid = models.CharField(db_column='TerminalID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    terminaldate = models.CharField(db_column='TerminalDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    terminaluserid = models.CharField(db_column='TerminalUserID', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    originalrefno = models.CharField(db_column='OriginalRefNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    originalamount = models.DecimalField(db_column='OriginalAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discountamount = models.DecimalField(db_column='DiscountAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discountpercent = models.DecimalField(db_column='DiscountPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalamount = models.DecimalField(db_column='TotalAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    redeemamount = models.DecimalField(db_column='RedeemAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pointopening = models.DecimalField(db_column='PointOpening', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pointaward = models.DecimalField(db_column='PointAward', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pointredeem = models.DecimalField(db_column='PointRedeem', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pointbalance = models.DecimalField(db_column='PointBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'clTerminalTxn'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    model = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')
    session_data = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Ilogtbl(models.Model):
    salesno = models.CharField(db_column='SalesNo', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    xmlparameter = models.TextField(db_column='XMLParameter', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'iLogTbl'


class Ilogtblerror(models.Model):
    salesno = models.CharField(db_column='SalesNo', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    xmlparameter = models.TextField(db_column='XMLParameter', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'iLogTblError'


class Mssum110(models.Model):
    txnperpost = models.CharField(db_column='TxnPerPost', primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (TxnPerPost, CpnyID, SiteID, BinCode, VendID, TxnDate, ItemType, InvtID) found, that is not supported. The first column is selected.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    siteid = models.CharField(db_column='SiteID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    bincode = models.CharField(db_column='BinCode', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    vendid = models.CharField(db_column='VendID', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txndate = models.CharField(db_column='TxnDate', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    itemtype = models.SmallIntegerField(db_column='ItemType')  # Field name made lowercase.
    invtid = models.CharField(db_column='InvtID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salesqty = models.DecimalField(db_column='SalesQty', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesdueamt = models.DecimalField(db_column='SalesDueAmt', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesuser1 = models.DecimalField(db_column='SalesUser1', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesuser2 = models.DecimalField(db_column='SalesUser2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    returnqty = models.DecimalField(db_column='ReturnQty', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    returndueamt = models.DecimalField(db_column='ReturnDueAmt', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    returnuser1 = models.DecimalField(db_column='ReturnUser1', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    returnuser2 = models.DecimalField(db_column='ReturnUser2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user1 = models.DecimalField(db_column='User1', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user2 = models.DecimalField(db_column='User2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user3 = models.DecimalField(db_column='User3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user4 = models.DecimalField(db_column='User4', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.
    qty00 = models.DecimalField(db_column='Qty00', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qty01 = models.DecimalField(db_column='Qty01', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qty02 = models.DecimalField(db_column='Qty02', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qty03 = models.DecimalField(db_column='Qty03', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qty04 = models.DecimalField(db_column='Qty04', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qty05 = models.DecimalField(db_column='Qty05', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qty06 = models.DecimalField(db_column='Qty06', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qty07 = models.DecimalField(db_column='Qty07', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qty08 = models.DecimalField(db_column='Qty08', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qty09 = models.DecimalField(db_column='Qty09', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qty10 = models.DecimalField(db_column='Qty10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qty11 = models.DecimalField(db_column='Qty11', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qty12 = models.DecimalField(db_column='Qty12', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qty13 = models.DecimalField(db_column='Qty13', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qty14 = models.DecimalField(db_column='Qty14', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qty15 = models.DecimalField(db_column='Qty15', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qty16 = models.DecimalField(db_column='Qty16', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qty17 = models.DecimalField(db_column='Qty17', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qty18 = models.DecimalField(db_column='Qty18', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qty19 = models.DecimalField(db_column='Qty19', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qty20 = models.DecimalField(db_column='Qty20', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qty21 = models.DecimalField(db_column='Qty21', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qty22 = models.DecimalField(db_column='Qty22', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qty23 = models.DecimalField(db_column='Qty23', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qty24 = models.DecimalField(db_column='Qty24', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt00 = models.DecimalField(db_column='Amt00', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt01 = models.DecimalField(db_column='Amt01', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt02 = models.DecimalField(db_column='Amt02', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt03 = models.DecimalField(db_column='Amt03', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt04 = models.DecimalField(db_column='Amt04', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt05 = models.DecimalField(db_column='Amt05', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt06 = models.DecimalField(db_column='Amt06', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt07 = models.DecimalField(db_column='Amt07', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt08 = models.DecimalField(db_column='Amt08', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt09 = models.DecimalField(db_column='Amt09', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt10 = models.DecimalField(db_column='Amt10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt11 = models.DecimalField(db_column='Amt11', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt12 = models.DecimalField(db_column='Amt12', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt13 = models.DecimalField(db_column='Amt13', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt14 = models.DecimalField(db_column='Amt14', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt15 = models.DecimalField(db_column='Amt15', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt16 = models.DecimalField(db_column='Amt16', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt17 = models.DecimalField(db_column='Amt17', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt18 = models.DecimalField(db_column='Amt18', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt19 = models.DecimalField(db_column='Amt19', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt20 = models.DecimalField(db_column='Amt20', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt21 = models.DecimalField(db_column='Amt21', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt22 = models.DecimalField(db_column='Amt22', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt23 = models.DecimalField(db_column='Amt23', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt24 = models.DecimalField(db_column='Amt24', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salespdamt = models.DecimalField(db_column='SalesPdAmt', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    returnpdamt = models.DecimalField(db_column='ReturnPdAmt', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'msSum110'
        unique_together = (('txnperpost', 'cpnyid', 'siteid', 'bincode', 'vendid', 'txndate', 'itemtype', 'invtid'),)


class Pscash(models.Model):
    cashno = models.CharField(db_column='CashNo', primary_key=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    siteid = models.CharField(db_column='SiteID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    terminalid = models.CharField(db_column='TerminalID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txndate = models.CharField(db_column='TxnDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txnempcode = models.CharField(db_column='TxnEmpCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salesdate = models.CharField(db_column='SalesDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cashierempcode = models.CharField(db_column='CashierEmpCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txntype = models.SmallIntegerField(db_column='TxnType')  # Field name made lowercase.
    currencyid = models.CharField(db_column='CurrencyID', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    totalamount = models.DecimalField(db_column='TotalAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    refno = models.CharField(db_column='RefNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descr = models.CharField(db_column='Descr', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psCash'


class Pscashitem(models.Model):
    cashno = models.CharField(db_column='CashNo', primary_key=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (CashNo, BillID) found, that is not supported. The first column is selected.
    billid = models.IntegerField(db_column='BillID')  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=19, decimal_places=4)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=19, decimal_places=4)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'psCashItem'
        unique_together = (('cashno', 'billid'),)


class Pscoupen(models.Model):
    coupenid = models.CharField(db_column='CoupenID', primary_key=True, max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    invtid = models.CharField(db_column='InvtID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    enabled = models.CharField(db_column='Enabled', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    begindate = models.CharField(db_column='BeginDate', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    enddate = models.CharField(db_column='EndDate', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    disamount = models.DecimalField(db_column='DisAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    dispercent = models.IntegerField(db_column='DisPercent')  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'psCoupen'


class Pscoupenhistory(models.Model):
    typeid = models.CharField(db_column='TypeID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    coupenid = models.CharField(db_column='CoupenID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    invtid = models.CharField(db_column='InvtID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    enabled = models.CharField(db_column='Enabled', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    begindate = models.CharField(db_column='BeginDate', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    enddate = models.CharField(db_column='EndDate', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    disamount = models.DecimalField(db_column='DisAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    dispercent = models.IntegerField(db_column='DisPercent')  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'psCoupenHistory'


class Pscoupen0516(models.Model):
    coupenid = models.CharField(db_column='CoupenID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    invtid = models.CharField(db_column='InvtID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    enabled = models.CharField(db_column='Enabled', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    begindate = models.CharField(db_column='BeginDate', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    enddate = models.CharField(db_column='EndDate', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    disamount = models.DecimalField(db_column='DisAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    dispercent = models.IntegerField(db_column='DisPercent')  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'psCoupen_0516'


class Psitemnoprice(models.Model):
    siteid = models.CharField(db_column='SiteID', primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (SiteID, TerminalID, InvtID, BarCode) found, that is not supported. The first column is selected.
    terminalid = models.CharField(db_column='TerminalID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    invtid = models.CharField(db_column='InvtID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    barcode = models.CharField(db_column='BarCode', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'psItemNoPrice'
        unique_together = (('siteid', 'terminalid', 'invtid', 'barcode'),)


class Pspaymentitem(models.Model):
    salesno = models.CharField(db_column='SalesNo', primary_key=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (SalesNo, LineNbr) found, that is not supported. The first column is selected.
    linenbr = models.SmallIntegerField(db_column='LineNbr')  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salesdate = models.CharField(db_column='SalesDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    paymenttypeid = models.CharField(db_column='PaymentTypeID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    detailtype = models.SmallIntegerField(db_column='DetailType')  # Field name made lowercase.
    currencyid = models.CharField(db_column='CurrencyID', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=19, decimal_places=4)  # Field name made lowercase.
    paymentamount = models.DecimalField(db_column='PaymentAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cardid = models.CharField(db_column='CardID', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cardexpiration = models.CharField(db_column='CardExpiration', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descr = models.CharField(db_column='Descr', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cardreference = models.CharField(db_column='CardReference', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.
    custid = models.CharField(db_column='CustID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    authcode = models.CharField(db_column='AuthCode', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psPaymentItem'
        unique_together = (('salesno', 'linenbr'),)


class Pspaymentitemarchive(models.Model):
    salesno = models.CharField(db_column='SalesNo', primary_key=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (SalesNo, LineNbr) found, that is not supported. The first column is selected.
    linenbr = models.SmallIntegerField(db_column='LineNbr')  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salesdate = models.CharField(db_column='SalesDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    paymenttypeid = models.CharField(db_column='PaymentTypeID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    detailtype = models.SmallIntegerField(db_column='DetailType')  # Field name made lowercase.
    currencyid = models.CharField(db_column='CurrencyID', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=19, decimal_places=4)  # Field name made lowercase.
    paymentamount = models.DecimalField(db_column='PaymentAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cardid = models.CharField(db_column='CardID', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cardexpiration = models.CharField(db_column='CardExpiration', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descr = models.CharField(db_column='Descr', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cardreference = models.CharField(db_column='CardReference', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'psPaymentItemArchive'
        unique_together = (('salesno', 'linenbr'),)


class Pspaymentitembank(models.Model):
    salesno = models.CharField(db_column='SalesNo', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    paymenttypeid = models.CharField(db_column='PaymentTypeID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    linenbr = models.SmallIntegerField(db_column='LineNbr')  # Field name made lowercase.
    authcode = models.CharField(db_column='AuthCode', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    opertype = models.CharField(db_column='OperType', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    input = models.CharField(db_column='Input', max_length=3000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    output = models.CharField(db_column='Output', max_length=3000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'psPaymentItemBank'


class PspaymentitembankHistory(models.Model):
    salesno = models.CharField(db_column='SalesNo', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    paymenttypeid = models.CharField(db_column='PaymentTypeID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    linenbr = models.SmallIntegerField(db_column='LineNbr')  # Field name made lowercase.
    authcode = models.CharField(db_column='AuthCode', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    opertype = models.CharField(db_column='OperType', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    input = models.CharField(db_column='Input', max_length=3000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    output = models.CharField(db_column='Output', max_length=3000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'psPaymentItemBank_History'


class Pspaymentitemdiff(models.Model):
    salesno = models.CharField(db_column='SalesNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    linenbr = models.SmallIntegerField(db_column='LineNbr')  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salesdate = models.CharField(db_column='SalesDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    paymenttypeid = models.CharField(db_column='PaymentTypeID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    detailtype = models.SmallIntegerField(db_column='DetailType')  # Field name made lowercase.
    currencyid = models.CharField(db_column='CurrencyID', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=19, decimal_places=4)  # Field name made lowercase.
    paymentamount = models.DecimalField(db_column='PaymentAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cardid = models.CharField(db_column='CardID', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cardexpiration = models.CharField(db_column='CardExpiration', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descr = models.CharField(db_column='Descr', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cardreference = models.CharField(db_column='CardReference', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.
    custid = models.CharField(db_column='CustID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    authcode = models.CharField(db_column='AuthCode', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psPaymentItemDiff'


class Pspaymentitemhold(models.Model):
    salesno = models.CharField(db_column='SalesNo', primary_key=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (SalesNo, LineNbr) found, that is not supported. The first column is selected.
    linenbr = models.SmallIntegerField(db_column='LineNbr')  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salesdate = models.CharField(db_column='SalesDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    paymenttypeid = models.CharField(db_column='PaymentTypeID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    detailtype = models.SmallIntegerField(db_column='DetailType')  # Field name made lowercase.
    currencyid = models.CharField(db_column='CurrencyID', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=19, decimal_places=4)  # Field name made lowercase.
    paymentamount = models.DecimalField(db_column='PaymentAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cardid = models.CharField(db_column='CardID', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cardexpiration = models.CharField(db_column='CardExpiration', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descr = models.CharField(db_column='Descr', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cardreference = models.CharField(db_column='CardReference', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.
    custid = models.CharField(db_column='CustID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psPaymentItemHold'
        unique_together = (('salesno', 'linenbr'),)


class Pspaymentitemloyalty(models.Model):
    salesno = models.CharField(db_column='SalesNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    linenbr = models.SmallIntegerField(db_column='LineNbr')  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salesdate = models.CharField(db_column='SalesDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    paymenttypeid = models.CharField(db_column='PaymentTypeID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    detailtype = models.SmallIntegerField(db_column='DetailType')  # Field name made lowercase.
    currencyid = models.CharField(db_column='CurrencyID', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=19, decimal_places=4)  # Field name made lowercase.
    paymentamount = models.DecimalField(db_column='PaymentAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cardid = models.CharField(db_column='CardID', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cardexpiration = models.CharField(db_column='CardExpiration', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descr = models.CharField(db_column='Descr', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cardreference = models.CharField(db_column='CardReference', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.
    custid = models.CharField(db_column='CustID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    authcode = models.CharField(db_column='AuthCode', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psPaymentItemLoyalty'


class Pspaymentitemvisa(models.Model):
    salesno = models.CharField(db_column='SalesNo', primary_key=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (SalesNo, LineNbr) found, that is not supported. The first column is selected.
    linenbr = models.SmallIntegerField(db_column='LineNbr')  # Field name made lowercase.
    salesdate = models.CharField(db_column='SalesDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    paymenttypeid = models.CharField(db_column='PaymentTypeID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txncode = models.CharField(db_column='TxnCode', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    merchant = models.CharField(db_column='Merchant', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    terminal = models.CharField(db_column='Terminal', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cardtype = models.CharField(db_column='CardType', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pan = models.CharField(db_column='PAN', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cardholder = models.CharField(db_column='CardHolder', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    expiration = models.CharField(db_column='Expiration', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    batch = models.CharField(db_column='Batch', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    trace = models.CharField(db_column='Trace', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    datetime = models.CharField(db_column='DateTime', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    reference = models.CharField(db_column='Reference', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    authorizationvisa = models.CharField(db_column='AuthorizationVISA', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    currencyname = models.CharField(db_column='CurrencyName', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    txnamount = models.DecimalField(db_column='TxnAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'psPaymentItemVISA'
        unique_together = (('salesno', 'linenbr'),)


class Pspostingsetup(models.Model):
    cpnyid = models.CharField(db_column='CpnyID', primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    autoposting = models.CharField(db_column='AutoPosting', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastrundate = models.CharField(db_column='LastRunDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lastduration = models.DecimalField(db_column='LastDuration', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lastresult = models.CharField(db_column='LastResult', max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.
    lastfullrundate = models.CharField(db_column='LastFullRunDate', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    usecostdate = models.CharField(db_column='UseCostDate', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psPostingSetup'


class Pssales(models.Model):
    salesno = models.CharField(db_column='SalesNo', primary_key=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    perpost = models.CharField(db_column='PerPost', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    siteid = models.CharField(db_column='SiteID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    terminalid = models.CharField(db_column='TerminalID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txndate = models.CharField(db_column='TxnDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txnempcode = models.CharField(db_column='TxnEmpCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salesdate = models.CharField(db_column='SalesDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cashierempcode = models.CharField(db_column='CashierEmpCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txntype = models.CharField(db_column='TxnType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salescount = models.IntegerField(db_column='SalesCount')  # Field name made lowercase.
    cardstatus = models.SmallIntegerField(db_column='CardStatus', blank=True, null=True)  # Field name made lowercase.
    cardid = models.CharField(db_column='CardID', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cardpercent = models.DecimalField(db_column='CardPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalcardpoint = models.DecimalField(db_column='TotalCardPoint', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatincluded = models.CharField(db_column='VATIncluded', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    vatpercent = models.DecimalField(db_column='VATPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesbonustype = models.CharField(db_column='SalesBonusType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salesbonuspercent = models.DecimalField(db_column='SalesBonusPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesbonusamount = models.DecimalField(db_column='SalesBonusAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesdiscounttype = models.CharField(db_column='SalesDiscountType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salesdiscountpercent = models.DecimalField(db_column='SalesDiscountPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesdiscountamount = models.DecimalField(db_column='SalesDiscountAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalsalesamount = models.DecimalField(db_column='TotalSalesAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalvatamount = models.DecimalField(db_column='TotalVATAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalsoldamount = models.DecimalField(db_column='TotalSoldAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalbonusamount = models.DecimalField(db_column='TotalBonusAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totaldiscountamount = models.DecimalField(db_column='TotalDiscountAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalcardamount = models.DecimalField(db_column='TotalCardAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totaldueamount = models.DecimalField(db_column='TotalDueAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalpaidamount = models.DecimalField(db_column='TotalPaidAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalcashamount = models.DecimalField(db_column='TotalCashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalnoncashamount = models.DecimalField(db_column='TotalNonCashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    refno = models.CharField(db_column='RefNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descr = models.CharField(db_column='Descr', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    summaryupdated = models.SmallIntegerField(db_column='SummaryUpdated', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    postingid = models.BigIntegerField(db_column='PostingID', blank=True, null=True)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.
    sicount = models.SmallIntegerField(db_column='SICount', blank=True, null=True)  # Field name made lowercase.
    picount = models.SmallIntegerField(db_column='PICount', blank=True, null=True)  # Field name made lowercase.
    periodyear = models.IntegerField(db_column='PeriodYear', blank=True, null=True)  # Field name made lowercase.
    totalpdsalesamount = models.DecimalField(db_column='TotalPdSalesAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalpricedownamount = models.DecimalField(db_column='TotalPriceDownAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalnhat = models.DecimalField(db_column='TotalNHAT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    custcpnyid = models.CharField(db_column='CustCpnyID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    custcpnyname = models.CharField(db_column='CustCpnyName', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ddtdno = models.CharField(db_column='DDTDNo', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccorder = models.CharField(db_column='ccOrder', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    returnreasonid = models.CharField(db_column='ReturnReasonID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    reasondescr = models.CharField(db_column='ReasonDescr', max_length=300, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    holddescr = models.CharField(db_column='HoldDescr', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psSales'


class Pssalesarchive(models.Model):
    salesno = models.CharField(db_column='SalesNo', primary_key=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    perpost = models.CharField(db_column='PerPost', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    siteid = models.CharField(db_column='SiteID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    terminalid = models.CharField(db_column='TerminalID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txndate = models.CharField(db_column='TxnDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txnempcode = models.CharField(db_column='TxnEmpCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salesdate = models.CharField(db_column='SalesDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cashierempcode = models.CharField(db_column='CashierEmpCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txntype = models.CharField(db_column='TxnType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salescount = models.IntegerField(db_column='SalesCount')  # Field name made lowercase.
    cardstatus = models.SmallIntegerField(db_column='CardStatus', blank=True, null=True)  # Field name made lowercase.
    cardid = models.CharField(db_column='CardID', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cardpercent = models.DecimalField(db_column='CardPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalcardpoint = models.DecimalField(db_column='TotalCardPoint', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatincluded = models.CharField(db_column='VATIncluded', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    vatpercent = models.DecimalField(db_column='VATPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesbonustype = models.CharField(db_column='SalesBonusType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salesbonuspercent = models.DecimalField(db_column='SalesBonusPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesbonusamount = models.DecimalField(db_column='SalesBonusAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesdiscounttype = models.CharField(db_column='SalesDiscountType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salesdiscountpercent = models.DecimalField(db_column='SalesDiscountPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesdiscountamount = models.DecimalField(db_column='SalesDiscountAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalsalesamount = models.DecimalField(db_column='TotalSalesAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalvatamount = models.DecimalField(db_column='TotalVATAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalsoldamount = models.DecimalField(db_column='TotalSoldAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalbonusamount = models.DecimalField(db_column='TotalBonusAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totaldiscountamount = models.DecimalField(db_column='TotalDiscountAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalcardamount = models.DecimalField(db_column='TotalCardAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totaldueamount = models.DecimalField(db_column='TotalDueAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalpaidamount = models.DecimalField(db_column='TotalPaidAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalcashamount = models.DecimalField(db_column='TotalCashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalnoncashamount = models.DecimalField(db_column='TotalNonCashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    refno = models.CharField(db_column='RefNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descr = models.CharField(db_column='Descr', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    summaryupdated = models.SmallIntegerField(db_column='SummaryUpdated', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    postingid = models.BigIntegerField(db_column='PostingID', blank=True, null=True)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.
    sicount = models.SmallIntegerField(db_column='SICount', blank=True, null=True)  # Field name made lowercase.
    picount = models.SmallIntegerField(db_column='PICount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psSalesArchive'


class Pssalesavailable(models.Model):
    salesno = models.CharField(db_column='SalesNo', primary_key=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (SalesNo, LineNbr) found, that is not supported. The first column is selected.
    linenbr = models.SmallIntegerField(db_column='LineNbr')  # Field name made lowercase.
    salesdate = models.CharField(db_column='SalesDate', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    siteid = models.CharField(db_column='SiteID', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    bincode = models.CharField(db_column='BinCode', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    invtid = models.CharField(db_column='InvtID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psSalesAvailable'
        unique_together = (('salesno', 'linenbr'),)


class Pssalescustinfo(models.Model):
    salesno = models.CharField(db_column='SalesNo', primary_key=True, max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    citizenship = models.CharField(db_column='Citizenship', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    regno = models.CharField(db_column='RegNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    seatno = models.CharField(db_column='SeatNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tocountry = models.CharField(db_column='ToCountry', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vehiclelicenseno = models.CharField(db_column='VehicleLicenseNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vehiclechasesno = models.CharField(db_column='VehicleChasesNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vehiclemanufacturer = models.CharField(db_column='VehicleManufacturer', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vehiclemodel = models.CharField(db_column='VehicleModel', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vehiclemodelyear = models.CharField(db_column='VehicleModelYear', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vehiclemileage = models.CharField(db_column='VehicleMileage', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vehicleenginecap = models.CharField(db_column='VehicleEngineCap', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vehiclefueltype = models.CharField(db_column='VehicleFuelType', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vehiclesteeringside = models.CharField(db_column='VehicleSteeringSide', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    custphone = models.CharField(db_column='CustPhone', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    custemail = models.CharField(db_column='CustEmail', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descr = models.CharField(db_column='Descr', max_length=600, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'psSalesCustInfo'


class Pssalesdiff(models.Model):
    salesno = models.CharField(db_column='SalesNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    perpost = models.CharField(db_column='PerPost', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    siteid = models.CharField(db_column='SiteID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    terminalid = models.CharField(db_column='TerminalID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txndate = models.CharField(db_column='TxnDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txnempcode = models.CharField(db_column='TxnEmpCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salesdate = models.CharField(db_column='SalesDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cashierempcode = models.CharField(db_column='CashierEmpCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txntype = models.CharField(db_column='TxnType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salescount = models.IntegerField(db_column='SalesCount')  # Field name made lowercase.
    cardstatus = models.SmallIntegerField(db_column='CardStatus', blank=True, null=True)  # Field name made lowercase.
    cardid = models.CharField(db_column='CardID', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cardpercent = models.DecimalField(db_column='CardPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalcardpoint = models.DecimalField(db_column='TotalCardPoint', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatincluded = models.CharField(db_column='VATIncluded', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    vatpercent = models.DecimalField(db_column='VATPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesbonustype = models.CharField(db_column='SalesBonusType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salesbonuspercent = models.DecimalField(db_column='SalesBonusPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesbonusamount = models.DecimalField(db_column='SalesBonusAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesdiscounttype = models.CharField(db_column='SalesDiscountType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salesdiscountpercent = models.DecimalField(db_column='SalesDiscountPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesdiscountamount = models.DecimalField(db_column='SalesDiscountAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalsalesamount = models.DecimalField(db_column='TotalSalesAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalvatamount = models.DecimalField(db_column='TotalVATAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalsoldamount = models.DecimalField(db_column='TotalSoldAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalbonusamount = models.DecimalField(db_column='TotalBonusAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totaldiscountamount = models.DecimalField(db_column='TotalDiscountAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalcardamount = models.DecimalField(db_column='TotalCardAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totaldueamount = models.DecimalField(db_column='TotalDueAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalpaidamount = models.DecimalField(db_column='TotalPaidAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalcashamount = models.DecimalField(db_column='TotalCashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalnoncashamount = models.DecimalField(db_column='TotalNonCashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    refno = models.CharField(db_column='RefNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descr = models.CharField(db_column='Descr', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    summaryupdated = models.SmallIntegerField(db_column='SummaryUpdated', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    postingid = models.BigIntegerField(db_column='PostingID', blank=True, null=True)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.
    sicount = models.SmallIntegerField(db_column='SICount', blank=True, null=True)  # Field name made lowercase.
    picount = models.SmallIntegerField(db_column='PICount', blank=True, null=True)  # Field name made lowercase.
    periodyear = models.IntegerField(db_column='PeriodYear', blank=True, null=True)  # Field name made lowercase.
    totalpdsalesamount = models.DecimalField(db_column='TotalPdSalesAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalpricedownamount = models.DecimalField(db_column='TotalPriceDownAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalnhat = models.DecimalField(db_column='TotalNHAT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    custcpnyid = models.CharField(db_column='CustCpnyID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    custcpnyname = models.CharField(db_column='CustCpnyName', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ddtdno = models.CharField(db_column='DDTDNo', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccorder = models.CharField(db_column='ccOrder', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psSalesDiff'


class Pssaleshold(models.Model):
    salesno = models.CharField(db_column='SalesNo', primary_key=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    perpost = models.CharField(db_column='PerPost', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    siteid = models.CharField(db_column='SiteID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    terminalid = models.CharField(db_column='TerminalID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txndate = models.CharField(db_column='TxnDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txnempcode = models.CharField(db_column='TxnEmpCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salesdate = models.CharField(db_column='SalesDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cashierempcode = models.CharField(db_column='CashierEmpCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txntype = models.CharField(db_column='TxnType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salescount = models.IntegerField(db_column='SalesCount')  # Field name made lowercase.
    cardstatus = models.SmallIntegerField(db_column='CardStatus', blank=True, null=True)  # Field name made lowercase.
    cardid = models.CharField(db_column='CardID', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cardpercent = models.DecimalField(db_column='CardPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalcardpoint = models.DecimalField(db_column='TotalCardPoint', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatincluded = models.CharField(db_column='VATIncluded', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    vatpercent = models.DecimalField(db_column='VATPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesbonustype = models.CharField(db_column='SalesBonusType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salesbonuspercent = models.DecimalField(db_column='SalesBonusPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesbonusamount = models.DecimalField(db_column='SalesBonusAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesdiscounttype = models.CharField(db_column='SalesDiscountType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salesdiscountpercent = models.DecimalField(db_column='SalesDiscountPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesdiscountamount = models.DecimalField(db_column='SalesDiscountAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalsalesamount = models.DecimalField(db_column='TotalSalesAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalvatamount = models.DecimalField(db_column='TotalVATAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalsoldamount = models.DecimalField(db_column='TotalSoldAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalbonusamount = models.DecimalField(db_column='TotalBonusAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totaldiscountamount = models.DecimalField(db_column='TotalDiscountAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalcardamount = models.DecimalField(db_column='TotalCardAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totaldueamount = models.DecimalField(db_column='TotalDueAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalpaidamount = models.DecimalField(db_column='TotalPaidAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalcashamount = models.DecimalField(db_column='TotalCashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalnoncashamount = models.DecimalField(db_column='TotalNonCashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    refno = models.CharField(db_column='RefNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descr = models.CharField(db_column='Descr', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    summaryupdated = models.SmallIntegerField(db_column='SummaryUpdated', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    postingid = models.BigIntegerField(db_column='PostingID', blank=True, null=True)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.
    totalpdsalesamount = models.DecimalField(db_column='TotalPdSalesAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalpricedownamount = models.DecimalField(db_column='TotalPriceDownAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psSalesHold'


class Pssalesitem(models.Model):
    salesno = models.CharField(db_column='SalesNo', primary_key=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (SalesNo, LineNbr) found, that is not supported. The first column is selected.
    linenbr = models.SmallIntegerField(db_column='LineNbr')  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salesdate = models.CharField(db_column='SalesDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    bincode = models.CharField(db_column='BinCode', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    itemtype = models.SmallIntegerField(db_column='ItemType')  # Field name made lowercase.
    invtid = models.CharField(db_column='InvtID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=19, decimal_places=4)  # Field name made lowercase.
    controlqty = models.DecimalField(db_column='ControlQty', max_digits=19, decimal_places=4)  # Field name made lowercase.
    qtystatus = models.SmallIntegerField(db_column='QtyStatus')  # Field name made lowercase.
    standardprice = models.DecimalField(db_column='StandardPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    saleprice = models.DecimalField(db_column='SalePrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salepricetype = models.DecimalField(db_column='SalePriceType', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wholeqty = models.DecimalField(db_column='WholeQty', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wholeprice = models.DecimalField(db_column='WholePrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    specialprice = models.DecimalField(db_column='SpecialPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemsalespricetype = models.SmallIntegerField(db_column='ItemSalesPriceType')  # Field name made lowercase.
    itemsalesprice = models.DecimalField(db_column='ItemSalesPrice', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemvatamount = models.DecimalField(db_column='ItemVATAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemsoldprice = models.DecimalField(db_column='ItemSoldPrice', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemsoldamount = models.DecimalField(db_column='ItemSoldAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itembonustype = models.CharField(db_column='ItemBonusType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itembonuspercent = models.DecimalField(db_column='ItemBonusPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itembonusamount = models.DecimalField(db_column='ItemBonusAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemdiscounttype = models.CharField(db_column='ItemDiscountType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itemdiscountpercent = models.DecimalField(db_column='ItemDiscountPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemdiscountamount = models.DecimalField(db_column='ItemDiscountAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemcardpercent = models.DecimalField(db_column='ItemCardPercent', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemcardamount = models.DecimalField(db_column='ItemCardAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemdueamount = models.DecimalField(db_column='ItemDueAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemcashamount = models.DecimalField(db_column='ItemCashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemnoncashamount = models.DecimalField(db_column='ItemNonCashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bonusid = models.BigIntegerField(db_column='BonusID', blank=True, null=True)  # Field name made lowercase.
    bonuslinenbr = models.SmallIntegerField(db_column='BonusLineNbr', blank=True, null=True)  # Field name made lowercase.
    bonpkgid = models.SmallIntegerField(db_column='BonPkgID', blank=True, null=True)  # Field name made lowercase.
    bonpkglinenbr = models.SmallIntegerField(db_column='BonPkgLineNbr', blank=True, null=True)  # Field name made lowercase.
    pendingpkgid = models.IntegerField(db_column='PendingPkgID', blank=True, null=True)  # Field name made lowercase.
    pendingbonqty = models.IntegerField(db_column='PendingBonQty', blank=True, null=True)  # Field name made lowercase.
    classid = models.CharField(db_column='ClassID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    invtdescr = models.CharField(db_column='InvtDescr', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    invtdescreng = models.CharField(db_column='InvtDescrEng', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='BarCode', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    baseunitid = models.CharField(db_column='BaseUnitID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    unitid = models.CharField(db_column='UnitID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    qtyperunit = models.DecimalField(db_column='QtyPerUnit', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    allowfractional = models.CharField(db_column='AllowFractional', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    postingdescr = models.CharField(db_column='PostingDescr', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.
    user1 = models.TextField(db_column='User1', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user2 = models.TextField(db_column='User2', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user3 = models.TextField(db_column='User3', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user4 = models.TextField(db_column='User4', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user5 = models.TextField(db_column='User5', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user6 = models.DecimalField(db_column='User6', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user7 = models.DecimalField(db_column='User7', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user8 = models.DecimalField(db_column='User8', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user9 = models.DecimalField(db_column='User9', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user10 = models.DecimalField(db_column='User10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vendid = models.CharField(db_column='VendID', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    periodyear = models.IntegerField(db_column='PeriodYear', blank=True, null=True)  # Field name made lowercase.
    pdtxnid = models.BigIntegerField(db_column='PdTxnID', blank=True, null=True)  # Field name made lowercase.
    pdorderno = models.CharField(db_column='PdOrderNo', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pdorderitemid = models.BigIntegerField(db_column='PdOrderItemID', blank=True, null=True)  # Field name made lowercase.
    pdordqty = models.DecimalField(db_column='PdOrdQty', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdtxncostid = models.BigIntegerField(db_column='PdTxnCostID', blank=True, null=True)  # Field name made lowercase.
    pdunitcost = models.DecimalField(db_column='PdUnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdstandardprice = models.DecimalField(db_column='PdStandardPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdlabelcode = models.CharField(db_column='PdLabelCode', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pdlabelpercent = models.DecimalField(db_column='PdLabelPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdqty = models.DecimalField(db_column='PdQty', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdsalesunitprice = models.DecimalField(db_column='PdSalesUnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdsalesamount = models.DecimalField(db_column='PdSalesAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricedownunitprice = models.DecimalField(db_column='PriceDownUnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricedownamount = models.DecimalField(db_column='PriceDownAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nhatamt = models.DecimalField(db_column='NHATAmt', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    isnhat = models.CharField(db_column='IsNHAT', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    noatusregno = models.CharField(db_column='NoatusRegNo', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    isnoatus = models.CharField(db_column='isNoatus', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    actionempcode = models.CharField(db_column='ActionEmpCode', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coupenid = models.CharField(db_column='CoupenID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    orginvtid = models.CharField(db_column='OrgInvtID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    switchqty = models.DecimalField(db_column='SwitchQty', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psSalesItem'
        unique_together = (('salesno', 'linenbr'),)


class Pssalesitemarchive(models.Model):
    salesno = models.CharField(db_column='SalesNo', primary_key=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (SalesNo, LineNbr) found, that is not supported. The first column is selected.
    linenbr = models.SmallIntegerField(db_column='LineNbr')  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salesdate = models.CharField(db_column='SalesDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    bincode = models.CharField(db_column='BinCode', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    itemtype = models.SmallIntegerField(db_column='ItemType')  # Field name made lowercase.
    invtid = models.CharField(db_column='InvtID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=19, decimal_places=4)  # Field name made lowercase.
    controlqty = models.DecimalField(db_column='ControlQty', max_digits=19, decimal_places=4)  # Field name made lowercase.
    qtystatus = models.SmallIntegerField(db_column='QtyStatus')  # Field name made lowercase.
    standardprice = models.DecimalField(db_column='StandardPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    saleprice = models.DecimalField(db_column='SalePrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salepricetype = models.DecimalField(db_column='SalePriceType', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wholeqty = models.DecimalField(db_column='WholeQty', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wholeprice = models.DecimalField(db_column='WholePrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    specialprice = models.DecimalField(db_column='SpecialPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemsalespricetype = models.SmallIntegerField(db_column='ItemSalesPriceType')  # Field name made lowercase.
    itemsalesprice = models.DecimalField(db_column='ItemSalesPrice', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemvatamount = models.DecimalField(db_column='ItemVATAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemsoldprice = models.DecimalField(db_column='ItemSoldPrice', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemsoldamount = models.DecimalField(db_column='ItemSoldAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itembonustype = models.CharField(db_column='ItemBonusType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itembonuspercent = models.DecimalField(db_column='ItemBonusPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itembonusamount = models.DecimalField(db_column='ItemBonusAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemdiscounttype = models.CharField(db_column='ItemDiscountType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itemdiscountpercent = models.DecimalField(db_column='ItemDiscountPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemdiscountamount = models.DecimalField(db_column='ItemDiscountAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemcardpercent = models.DecimalField(db_column='ItemCardPercent', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemcardamount = models.DecimalField(db_column='ItemCardAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemdueamount = models.DecimalField(db_column='ItemDueAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemcashamount = models.DecimalField(db_column='ItemCashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemnoncashamount = models.DecimalField(db_column='ItemNonCashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bonusid = models.BigIntegerField(db_column='BonusID', blank=True, null=True)  # Field name made lowercase.
    bonuslinenbr = models.SmallIntegerField(db_column='BonusLineNbr', blank=True, null=True)  # Field name made lowercase.
    bonpkgid = models.SmallIntegerField(db_column='BonPkgID', blank=True, null=True)  # Field name made lowercase.
    bonpkglinenbr = models.SmallIntegerField(db_column='BonPkgLineNbr', blank=True, null=True)  # Field name made lowercase.
    pendingpkgid = models.IntegerField(db_column='PendingPkgID', blank=True, null=True)  # Field name made lowercase.
    pendingbonqty = models.IntegerField(db_column='PendingBonQty', blank=True, null=True)  # Field name made lowercase.
    classid = models.CharField(db_column='ClassID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    invtdescr = models.CharField(db_column='InvtDescr', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    invtdescreng = models.CharField(db_column='InvtDescrEng', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='BarCode', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    baseunitid = models.CharField(db_column='BaseUnitID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    unitid = models.CharField(db_column='UnitID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    qtyperunit = models.DecimalField(db_column='QtyPerUnit', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    allowfractional = models.CharField(db_column='AllowFractional', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    postingdescr = models.CharField(db_column='PostingDescr', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'psSalesItemArchive'
        unique_together = (('salesno', 'linenbr'),)


class Pssalesitemdiff(models.Model):
    salesno = models.CharField(db_column='SalesNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    linenbr = models.SmallIntegerField(db_column='LineNbr')  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salesdate = models.CharField(db_column='SalesDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    bincode = models.CharField(db_column='BinCode', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    itemtype = models.SmallIntegerField(db_column='ItemType')  # Field name made lowercase.
    invtid = models.CharField(db_column='InvtID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=19, decimal_places=4)  # Field name made lowercase.
    controlqty = models.DecimalField(db_column='ControlQty', max_digits=19, decimal_places=4)  # Field name made lowercase.
    qtystatus = models.SmallIntegerField(db_column='QtyStatus')  # Field name made lowercase.
    standardprice = models.DecimalField(db_column='StandardPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    saleprice = models.DecimalField(db_column='SalePrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salepricetype = models.DecimalField(db_column='SalePriceType', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wholeqty = models.DecimalField(db_column='WholeQty', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wholeprice = models.DecimalField(db_column='WholePrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    specialprice = models.DecimalField(db_column='SpecialPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemsalespricetype = models.SmallIntegerField(db_column='ItemSalesPriceType')  # Field name made lowercase.
    itemsalesprice = models.DecimalField(db_column='ItemSalesPrice', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemvatamount = models.DecimalField(db_column='ItemVATAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemsoldprice = models.DecimalField(db_column='ItemSoldPrice', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemsoldamount = models.DecimalField(db_column='ItemSoldAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itembonustype = models.CharField(db_column='ItemBonusType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itembonuspercent = models.DecimalField(db_column='ItemBonusPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itembonusamount = models.DecimalField(db_column='ItemBonusAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemdiscounttype = models.CharField(db_column='ItemDiscountType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itemdiscountpercent = models.DecimalField(db_column='ItemDiscountPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemdiscountamount = models.DecimalField(db_column='ItemDiscountAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemcardpercent = models.DecimalField(db_column='ItemCardPercent', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemcardamount = models.DecimalField(db_column='ItemCardAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemdueamount = models.DecimalField(db_column='ItemDueAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemcashamount = models.DecimalField(db_column='ItemCashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemnoncashamount = models.DecimalField(db_column='ItemNonCashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bonusid = models.BigIntegerField(db_column='BonusID', blank=True, null=True)  # Field name made lowercase.
    bonuslinenbr = models.SmallIntegerField(db_column='BonusLineNbr', blank=True, null=True)  # Field name made lowercase.
    bonpkgid = models.SmallIntegerField(db_column='BonPkgID', blank=True, null=True)  # Field name made lowercase.
    bonpkglinenbr = models.SmallIntegerField(db_column='BonPkgLineNbr', blank=True, null=True)  # Field name made lowercase.
    pendingpkgid = models.IntegerField(db_column='PendingPkgID', blank=True, null=True)  # Field name made lowercase.
    pendingbonqty = models.IntegerField(db_column='PendingBonQty', blank=True, null=True)  # Field name made lowercase.
    classid = models.CharField(db_column='ClassID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    invtdescr = models.CharField(db_column='InvtDescr', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    invtdescreng = models.CharField(db_column='InvtDescrEng', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='BarCode', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    baseunitid = models.CharField(db_column='BaseUnitID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    unitid = models.CharField(db_column='UnitID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    qtyperunit = models.DecimalField(db_column='QtyPerUnit', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    allowfractional = models.CharField(db_column='AllowFractional', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    postingdescr = models.CharField(db_column='PostingDescr', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.
    user1 = models.TextField(db_column='User1', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user2 = models.TextField(db_column='User2', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user3 = models.TextField(db_column='User3', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user4 = models.TextField(db_column='User4', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user5 = models.TextField(db_column='User5', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user6 = models.DecimalField(db_column='User6', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user7 = models.DecimalField(db_column='User7', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user8 = models.DecimalField(db_column='User8', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user9 = models.DecimalField(db_column='User9', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user10 = models.DecimalField(db_column='User10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vendid = models.CharField(db_column='VendID', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    periodyear = models.IntegerField(db_column='PeriodYear', blank=True, null=True)  # Field name made lowercase.
    pdtxnid = models.BigIntegerField(db_column='PdTxnID', blank=True, null=True)  # Field name made lowercase.
    pdorderno = models.CharField(db_column='PdOrderNo', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pdorderitemid = models.BigIntegerField(db_column='PdOrderItemID', blank=True, null=True)  # Field name made lowercase.
    pdordqty = models.DecimalField(db_column='PdOrdQty', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdtxncostid = models.BigIntegerField(db_column='PdTxnCostID', blank=True, null=True)  # Field name made lowercase.
    pdunitcost = models.DecimalField(db_column='PdUnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdstandardprice = models.DecimalField(db_column='PdStandardPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdlabelcode = models.CharField(db_column='PdLabelCode', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pdlabelpercent = models.DecimalField(db_column='PdLabelPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdqty = models.DecimalField(db_column='PdQty', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdsalesunitprice = models.DecimalField(db_column='PdSalesUnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdsalesamount = models.DecimalField(db_column='PdSalesAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricedownunitprice = models.DecimalField(db_column='PriceDownUnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricedownamount = models.DecimalField(db_column='PriceDownAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nhatamt = models.DecimalField(db_column='NHATAmt', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    isnhat = models.CharField(db_column='IsNHAT', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    noatusregno = models.CharField(db_column='NoatusRegNo', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    isnoatus = models.CharField(db_column='isNoatus', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    actionempcode = models.CharField(db_column='ActionEmpCode', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coupenid = models.CharField(db_column='CoupenID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psSalesItemDiff'


class Pssalesitemhold(models.Model):
    salesno = models.CharField(db_column='SalesNo', primary_key=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (SalesNo, LineNbr) found, that is not supported. The first column is selected.
    linenbr = models.SmallIntegerField(db_column='LineNbr')  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salesdate = models.CharField(db_column='SalesDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    bincode = models.CharField(db_column='BinCode', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    itemtype = models.SmallIntegerField(db_column='ItemType')  # Field name made lowercase.
    invtid = models.CharField(db_column='InvtID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=19, decimal_places=4)  # Field name made lowercase.
    controlqty = models.DecimalField(db_column='ControlQty', max_digits=19, decimal_places=4)  # Field name made lowercase.
    qtystatus = models.SmallIntegerField(db_column='QtyStatus')  # Field name made lowercase.
    standardprice = models.DecimalField(db_column='StandardPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    saleprice = models.DecimalField(db_column='SalePrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salepricetype = models.DecimalField(db_column='SalePriceType', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wholeqty = models.DecimalField(db_column='WholeQty', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wholeprice = models.DecimalField(db_column='WholePrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    specialprice = models.DecimalField(db_column='SpecialPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemsalespricetype = models.SmallIntegerField(db_column='ItemSalesPriceType')  # Field name made lowercase.
    itemsalesprice = models.DecimalField(db_column='ItemSalesPrice', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemvatamount = models.DecimalField(db_column='ItemVATAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemsoldprice = models.DecimalField(db_column='ItemSoldPrice', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemsoldamount = models.DecimalField(db_column='ItemSoldAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itembonustype = models.CharField(db_column='ItemBonusType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itembonuspercent = models.DecimalField(db_column='ItemBonusPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itembonusamount = models.DecimalField(db_column='ItemBonusAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemdiscounttype = models.CharField(db_column='ItemDiscountType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itemdiscountpercent = models.DecimalField(db_column='ItemDiscountPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemdiscountamount = models.DecimalField(db_column='ItemDiscountAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemcardpercent = models.DecimalField(db_column='ItemCardPercent', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemcardamount = models.DecimalField(db_column='ItemCardAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemdueamount = models.DecimalField(db_column='ItemDueAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemcashamount = models.DecimalField(db_column='ItemCashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemnoncashamount = models.DecimalField(db_column='ItemNonCashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bonusid = models.BigIntegerField(db_column='BonusID', blank=True, null=True)  # Field name made lowercase.
    bonuslinenbr = models.SmallIntegerField(db_column='BonusLineNbr', blank=True, null=True)  # Field name made lowercase.
    bonpkgid = models.SmallIntegerField(db_column='BonPkgID', blank=True, null=True)  # Field name made lowercase.
    bonpkglinenbr = models.SmallIntegerField(db_column='BonPkgLineNbr', blank=True, null=True)  # Field name made lowercase.
    pendingpkgid = models.IntegerField(db_column='PendingPkgID', blank=True, null=True)  # Field name made lowercase.
    pendingbonqty = models.IntegerField(db_column='PendingBonQty', blank=True, null=True)  # Field name made lowercase.
    classid = models.CharField(db_column='ClassID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    invtdescr = models.CharField(db_column='InvtDescr', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    invtdescreng = models.CharField(db_column='InvtDescrEng', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='BarCode', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    baseunitid = models.CharField(db_column='BaseUnitID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    unitid = models.CharField(db_column='UnitID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    qtyperunit = models.DecimalField(db_column='QtyPerUnit', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    allowfractional = models.CharField(db_column='AllowFractional', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    postingdescr = models.CharField(db_column='PostingDescr', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.
    user1 = models.TextField(db_column='User1', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user2 = models.TextField(db_column='User2', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user3 = models.TextField(db_column='User3', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user4 = models.TextField(db_column='User4', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user5 = models.TextField(db_column='User5', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user6 = models.DecimalField(db_column='User6', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user7 = models.DecimalField(db_column='User7', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user8 = models.DecimalField(db_column='User8', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user9 = models.DecimalField(db_column='User9', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user10 = models.DecimalField(db_column='User10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vendid = models.CharField(db_column='VendID', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pdtxnid = models.BigIntegerField(db_column='PdTxnID', blank=True, null=True)  # Field name made lowercase.
    pdorderno = models.CharField(db_column='PdOrderNo', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pdorderitemid = models.BigIntegerField(db_column='PdOrderItemID', blank=True, null=True)  # Field name made lowercase.
    pdordqty = models.DecimalField(db_column='PdOrdQty', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdtxncostid = models.BigIntegerField(db_column='PdTxnCostID', blank=True, null=True)  # Field name made lowercase.
    pdunitcost = models.DecimalField(db_column='PdUnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdstandardprice = models.DecimalField(db_column='PdStandardPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdlabelcode = models.CharField(db_column='PdLabelCode', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pdlabelpercent = models.DecimalField(db_column='PdLabelPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdqty = models.DecimalField(db_column='PdQty', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdsalesunitprice = models.DecimalField(db_column='PdSalesUnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdsalesamount = models.DecimalField(db_column='PdSalesAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricedownunitprice = models.DecimalField(db_column='PriceDownUnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricedownamount = models.DecimalField(db_column='PriceDownAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemfsoldprice = models.DecimalField(db_column='ItemFSoldPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psSalesItemHold'
        unique_together = (('salesno', 'linenbr'),)


class Pssalesitem0415(models.Model):
    salesno = models.CharField(db_column='SalesNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    linenbr = models.SmallIntegerField(db_column='LineNbr')  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salesdate = models.CharField(db_column='SalesDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    bincode = models.CharField(db_column='BinCode', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    itemtype = models.SmallIntegerField(db_column='ItemType')  # Field name made lowercase.
    invtid = models.CharField(db_column='InvtID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=19, decimal_places=4)  # Field name made lowercase.
    controlqty = models.DecimalField(db_column='ControlQty', max_digits=19, decimal_places=4)  # Field name made lowercase.
    qtystatus = models.SmallIntegerField(db_column='QtyStatus')  # Field name made lowercase.
    standardprice = models.DecimalField(db_column='StandardPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    saleprice = models.DecimalField(db_column='SalePrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salepricetype = models.DecimalField(db_column='SalePriceType', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wholeqty = models.DecimalField(db_column='WholeQty', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wholeprice = models.DecimalField(db_column='WholePrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    specialprice = models.DecimalField(db_column='SpecialPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemsalespricetype = models.SmallIntegerField(db_column='ItemSalesPriceType')  # Field name made lowercase.
    itemsalesprice = models.DecimalField(db_column='ItemSalesPrice', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemvatamount = models.DecimalField(db_column='ItemVATAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemsoldprice = models.DecimalField(db_column='ItemSoldPrice', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemsoldamount = models.DecimalField(db_column='ItemSoldAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itembonustype = models.CharField(db_column='ItemBonusType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itembonuspercent = models.DecimalField(db_column='ItemBonusPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itembonusamount = models.DecimalField(db_column='ItemBonusAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemdiscounttype = models.CharField(db_column='ItemDiscountType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itemdiscountpercent = models.DecimalField(db_column='ItemDiscountPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemdiscountamount = models.DecimalField(db_column='ItemDiscountAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemcardpercent = models.DecimalField(db_column='ItemCardPercent', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemcardamount = models.DecimalField(db_column='ItemCardAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemdueamount = models.DecimalField(db_column='ItemDueAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemcashamount = models.DecimalField(db_column='ItemCashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemnoncashamount = models.DecimalField(db_column='ItemNonCashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bonusid = models.BigIntegerField(db_column='BonusID', blank=True, null=True)  # Field name made lowercase.
    bonuslinenbr = models.SmallIntegerField(db_column='BonusLineNbr', blank=True, null=True)  # Field name made lowercase.
    bonpkgid = models.SmallIntegerField(db_column='BonPkgID', blank=True, null=True)  # Field name made lowercase.
    bonpkglinenbr = models.SmallIntegerField(db_column='BonPkgLineNbr', blank=True, null=True)  # Field name made lowercase.
    pendingpkgid = models.IntegerField(db_column='PendingPkgID', blank=True, null=True)  # Field name made lowercase.
    pendingbonqty = models.IntegerField(db_column='PendingBonQty', blank=True, null=True)  # Field name made lowercase.
    classid = models.CharField(db_column='ClassID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    invtdescr = models.CharField(db_column='InvtDescr', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    invtdescreng = models.CharField(db_column='InvtDescrEng', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='BarCode', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    baseunitid = models.CharField(db_column='BaseUnitID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    unitid = models.CharField(db_column='UnitID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    qtyperunit = models.DecimalField(db_column='QtyPerUnit', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    allowfractional = models.CharField(db_column='AllowFractional', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    postingdescr = models.CharField(db_column='PostingDescr', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.
    user1 = models.TextField(db_column='User1', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user2 = models.TextField(db_column='User2', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user3 = models.TextField(db_column='User3', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user4 = models.TextField(db_column='User4', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user5 = models.TextField(db_column='User5', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user6 = models.DecimalField(db_column='User6', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user7 = models.DecimalField(db_column='User7', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user8 = models.DecimalField(db_column='User8', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user9 = models.DecimalField(db_column='User9', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user10 = models.DecimalField(db_column='User10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vendid = models.CharField(db_column='VendID', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    periodyear = models.IntegerField(db_column='PeriodYear', blank=True, null=True)  # Field name made lowercase.
    pdtxnid = models.BigIntegerField(db_column='PdTxnID', blank=True, null=True)  # Field name made lowercase.
    pdorderno = models.CharField(db_column='PdOrderNo', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pdorderitemid = models.BigIntegerField(db_column='PdOrderItemID', blank=True, null=True)  # Field name made lowercase.
    pdordqty = models.DecimalField(db_column='PdOrdQty', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdtxncostid = models.BigIntegerField(db_column='PdTxnCostID', blank=True, null=True)  # Field name made lowercase.
    pdunitcost = models.DecimalField(db_column='PdUnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdstandardprice = models.DecimalField(db_column='PdStandardPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdlabelcode = models.CharField(db_column='PdLabelCode', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pdlabelpercent = models.DecimalField(db_column='PdLabelPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdqty = models.DecimalField(db_column='PdQty', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdsalesunitprice = models.DecimalField(db_column='PdSalesUnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdsalesamount = models.DecimalField(db_column='PdSalesAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricedownunitprice = models.DecimalField(db_column='PriceDownUnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricedownamount = models.DecimalField(db_column='PriceDownAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nhatamt = models.DecimalField(db_column='NHATAmt', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    isnhat = models.CharField(db_column='IsNHAT', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    noatusregno = models.CharField(db_column='NoatusRegNo', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    isnoatus = models.CharField(db_column='isNoatus', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    actionempcode = models.CharField(db_column='ActionEmpCode', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psSalesItem_0415'


class Pssalesitem0511(models.Model):
    salesno = models.CharField(db_column='SalesNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    linenbr = models.SmallIntegerField(db_column='LineNbr')  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salesdate = models.CharField(db_column='SalesDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    bincode = models.CharField(db_column='BinCode', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    itemtype = models.SmallIntegerField(db_column='ItemType')  # Field name made lowercase.
    invtid = models.CharField(db_column='InvtID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=19, decimal_places=4)  # Field name made lowercase.
    controlqty = models.DecimalField(db_column='ControlQty', max_digits=19, decimal_places=4)  # Field name made lowercase.
    qtystatus = models.SmallIntegerField(db_column='QtyStatus')  # Field name made lowercase.
    standardprice = models.DecimalField(db_column='StandardPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    saleprice = models.DecimalField(db_column='SalePrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salepricetype = models.DecimalField(db_column='SalePriceType', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wholeqty = models.DecimalField(db_column='WholeQty', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wholeprice = models.DecimalField(db_column='WholePrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    specialprice = models.DecimalField(db_column='SpecialPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemsalespricetype = models.SmallIntegerField(db_column='ItemSalesPriceType')  # Field name made lowercase.
    itemsalesprice = models.DecimalField(db_column='ItemSalesPrice', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemvatamount = models.DecimalField(db_column='ItemVATAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemsoldprice = models.DecimalField(db_column='ItemSoldPrice', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemsoldamount = models.DecimalField(db_column='ItemSoldAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itembonustype = models.CharField(db_column='ItemBonusType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itembonuspercent = models.DecimalField(db_column='ItemBonusPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itembonusamount = models.DecimalField(db_column='ItemBonusAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemdiscounttype = models.CharField(db_column='ItemDiscountType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itemdiscountpercent = models.DecimalField(db_column='ItemDiscountPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemdiscountamount = models.DecimalField(db_column='ItemDiscountAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemcardpercent = models.DecimalField(db_column='ItemCardPercent', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemcardamount = models.DecimalField(db_column='ItemCardAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemdueamount = models.DecimalField(db_column='ItemDueAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemcashamount = models.DecimalField(db_column='ItemCashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemnoncashamount = models.DecimalField(db_column='ItemNonCashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bonusid = models.BigIntegerField(db_column='BonusID', blank=True, null=True)  # Field name made lowercase.
    bonuslinenbr = models.SmallIntegerField(db_column='BonusLineNbr', blank=True, null=True)  # Field name made lowercase.
    bonpkgid = models.SmallIntegerField(db_column='BonPkgID', blank=True, null=True)  # Field name made lowercase.
    bonpkglinenbr = models.SmallIntegerField(db_column='BonPkgLineNbr', blank=True, null=True)  # Field name made lowercase.
    pendingpkgid = models.IntegerField(db_column='PendingPkgID', blank=True, null=True)  # Field name made lowercase.
    pendingbonqty = models.IntegerField(db_column='PendingBonQty', blank=True, null=True)  # Field name made lowercase.
    classid = models.CharField(db_column='ClassID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    invtdescr = models.CharField(db_column='InvtDescr', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    invtdescreng = models.CharField(db_column='InvtDescrEng', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='BarCode', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    baseunitid = models.CharField(db_column='BaseUnitID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    unitid = models.CharField(db_column='UnitID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    qtyperunit = models.DecimalField(db_column='QtyPerUnit', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    allowfractional = models.CharField(db_column='AllowFractional', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    postingdescr = models.CharField(db_column='PostingDescr', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    user1 = models.TextField(db_column='User1', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user2 = models.TextField(db_column='User2', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user3 = models.TextField(db_column='User3', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user4 = models.TextField(db_column='User4', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user5 = models.TextField(db_column='User5', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user6 = models.DecimalField(db_column='User6', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user7 = models.DecimalField(db_column='User7', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user8 = models.DecimalField(db_column='User8', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user9 = models.DecimalField(db_column='User9', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user10 = models.DecimalField(db_column='User10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vendid = models.CharField(db_column='VendID', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    periodyear = models.IntegerField(db_column='PeriodYear', blank=True, null=True)  # Field name made lowercase.
    pdtxnid = models.BigIntegerField(db_column='PdTxnID', blank=True, null=True)  # Field name made lowercase.
    pdorderno = models.CharField(db_column='PdOrderNo', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pdorderitemid = models.BigIntegerField(db_column='PdOrderItemID', blank=True, null=True)  # Field name made lowercase.
    pdordqty = models.DecimalField(db_column='PdOrdQty', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdtxncostid = models.BigIntegerField(db_column='PdTxnCostID', blank=True, null=True)  # Field name made lowercase.
    pdunitcost = models.DecimalField(db_column='PdUnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdstandardprice = models.DecimalField(db_column='PdStandardPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdlabelcode = models.CharField(db_column='PdLabelCode', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pdlabelpercent = models.DecimalField(db_column='PdLabelPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdqty = models.DecimalField(db_column='PdQty', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdsalesunitprice = models.DecimalField(db_column='PdSalesUnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pdsalesamount = models.DecimalField(db_column='PdSalesAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricedownunitprice = models.DecimalField(db_column='PriceDownUnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricedownamount = models.DecimalField(db_column='PriceDownAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nhatamt = models.DecimalField(db_column='NHATAmt', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    isnhat = models.CharField(db_column='IsNHAT', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    noatusregno = models.CharField(db_column='NoatusRegNo', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    isnoatus = models.CharField(db_column='isNoatus', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    actionempcode = models.CharField(db_column='ActionEmpCode', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psSalesItem_0511'


class Pssalesnuatus(models.Model):
    salesno = models.CharField(db_column='SalesNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    input = models.TextField(db_column='Input', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    output = models.TextField(db_column='Output', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'psSalesNuatus'


class Pssalesposting(models.Model):
    salesno = models.CharField(db_column='SalesNo', primary_key=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (SalesNo, LineNbr) found, that is not supported. The first column is selected.
    linenbr = models.SmallIntegerField(db_column='LineNbr')  # Field name made lowercase.
    txntype = models.CharField(db_column='TxnType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salesdate = models.CharField(db_column='SalesDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    siteid = models.CharField(db_column='SiteID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    bincode = models.CharField(db_column='BinCode', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    invtid = models.CharField(db_column='InvtID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=19, decimal_places=4)  # Field name made lowercase.
    postingdescr = models.CharField(db_column='PostingDescr', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.
    periodyear = models.IntegerField(db_column='PeriodYear', blank=True, null=True)  # Field name made lowercase.
    adjposting = models.CharField(db_column='AdjPosting', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    adjdescr = models.CharField(db_column='AdjDescr', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    assemposting = models.CharField(db_column='AssemPosting', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    retrycount = models.IntegerField(db_column='RetryCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psSalesPosting'
        unique_together = (('salesno', 'linenbr'),)


class Pssalespostinggl(models.Model):
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salesdate = models.CharField(db_column='SalesDate', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    siteid = models.CharField(db_column='SiteID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    postingid = models.IntegerField(db_column='PostingID')  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.
    postingdescr = models.CharField(db_column='PostingDescr', max_length=3500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    periodyear = models.IntegerField(db_column='PeriodYear', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psSalesPostingGL'


class Pssalespostinglog(models.Model):
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descr = models.CharField(db_column='Descr', max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    logdate = models.CharField(db_column='LogDate', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    begintxndate = models.CharField(db_column='BeginTxnDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    siteid = models.CharField(db_column='SiteID', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    begindate = models.CharField(db_column='BeginDate', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    enddate = models.CharField(db_column='EndDate', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salescount = models.IntegerField(db_column='SalesCount', blank=True, null=True)  # Field name made lowercase.
    txncount = models.IntegerField(db_column='TxnCount', blank=True, null=True)  # Field name made lowercase.
    lasttxndate = models.CharField(db_column='LastTxnDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psSalesPostingLOG'


class Pssalesprogram(models.Model):
    salesno = models.CharField(db_column='SalesNo', primary_key=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (SalesNo, ProgramCode, CheckText) found, that is not supported. The first column is selected.
    programcode = models.CharField(db_column='ProgramCode', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    checktext = models.CharField(db_column='CheckText', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    user1 = models.TextField(db_column='User1', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user2 = models.TextField(db_column='User2', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user3 = models.TextField(db_column='User3', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user4 = models.TextField(db_column='User4', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user5 = models.TextField(db_column='User5', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user6 = models.DecimalField(db_column='User6', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user7 = models.DecimalField(db_column='User7', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user8 = models.DecimalField(db_column='User8', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user9 = models.DecimalField(db_column='User9', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user10 = models.DecimalField(db_column='User10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'psSalesProgram'
        unique_together = (('salesno', 'programcode', 'checktext'),)


class Pssalesprogramhold(models.Model):
    salesno = models.CharField(db_column='SalesNo', primary_key=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (SalesNo, ProgramCode, CheckText) found, that is not supported. The first column is selected.
    programcode = models.CharField(db_column='ProgramCode', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    checktext = models.CharField(db_column='CheckText', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    user1 = models.TextField(db_column='User1', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user2 = models.TextField(db_column='User2', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user3 = models.TextField(db_column='User3', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user4 = models.TextField(db_column='User4', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user5 = models.TextField(db_column='User5', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user6 = models.DecimalField(db_column='User6', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user7 = models.DecimalField(db_column='User7', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user8 = models.DecimalField(db_column='User8', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user9 = models.DecimalField(db_column='User9', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user10 = models.DecimalField(db_column='User10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'psSalesProgramHold'
        unique_together = (('salesno', 'programcode', 'checktext'),)


class Pssales0415(models.Model):
    salesno = models.CharField(db_column='SalesNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    perpost = models.CharField(db_column='PerPost', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    siteid = models.CharField(db_column='SiteID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    terminalid = models.CharField(db_column='TerminalID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txndate = models.CharField(db_column='TxnDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txnempcode = models.CharField(db_column='TxnEmpCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salesdate = models.CharField(db_column='SalesDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cashierempcode = models.CharField(db_column='CashierEmpCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txntype = models.CharField(db_column='TxnType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salescount = models.IntegerField(db_column='SalesCount')  # Field name made lowercase.
    cardstatus = models.SmallIntegerField(db_column='CardStatus', blank=True, null=True)  # Field name made lowercase.
    cardid = models.CharField(db_column='CardID', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cardpercent = models.DecimalField(db_column='CardPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalcardpoint = models.DecimalField(db_column='TotalCardPoint', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatincluded = models.CharField(db_column='VATIncluded', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    vatpercent = models.DecimalField(db_column='VATPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesbonustype = models.CharField(db_column='SalesBonusType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salesbonuspercent = models.DecimalField(db_column='SalesBonusPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesbonusamount = models.DecimalField(db_column='SalesBonusAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesdiscounttype = models.CharField(db_column='SalesDiscountType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salesdiscountpercent = models.DecimalField(db_column='SalesDiscountPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesdiscountamount = models.DecimalField(db_column='SalesDiscountAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalsalesamount = models.DecimalField(db_column='TotalSalesAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalvatamount = models.DecimalField(db_column='TotalVATAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalsoldamount = models.DecimalField(db_column='TotalSoldAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalbonusamount = models.DecimalField(db_column='TotalBonusAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totaldiscountamount = models.DecimalField(db_column='TotalDiscountAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalcardamount = models.DecimalField(db_column='TotalCardAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totaldueamount = models.DecimalField(db_column='TotalDueAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalpaidamount = models.DecimalField(db_column='TotalPaidAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalcashamount = models.DecimalField(db_column='TotalCashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalnoncashamount = models.DecimalField(db_column='TotalNonCashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    refno = models.CharField(db_column='RefNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descr = models.CharField(db_column='Descr', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    summaryupdated = models.SmallIntegerField(db_column='SummaryUpdated', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    postingid = models.BigIntegerField(db_column='PostingID', blank=True, null=True)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.
    sicount = models.SmallIntegerField(db_column='SICount', blank=True, null=True)  # Field name made lowercase.
    picount = models.SmallIntegerField(db_column='PICount', blank=True, null=True)  # Field name made lowercase.
    periodyear = models.IntegerField(db_column='PeriodYear', blank=True, null=True)  # Field name made lowercase.
    totalpdsalesamount = models.DecimalField(db_column='TotalPdSalesAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalpricedownamount = models.DecimalField(db_column='TotalPriceDownAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalnhat = models.DecimalField(db_column='TotalNHAT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    custcpnyid = models.CharField(db_column='CustCpnyID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    custcpnyname = models.CharField(db_column='CustCpnyName', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ddtdno = models.CharField(db_column='DDTDNo', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccorder = models.CharField(db_column='ccOrder', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psSales_0415'


class Pssales0510(models.Model):
    salesno = models.CharField(db_column='SalesNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    perpost = models.CharField(db_column='PerPost', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    siteid = models.CharField(db_column='SiteID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    terminalid = models.CharField(db_column='TerminalID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txndate = models.CharField(db_column='TxnDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txnempcode = models.CharField(db_column='TxnEmpCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salesdate = models.CharField(db_column='SalesDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cashierempcode = models.CharField(db_column='CashierEmpCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txntype = models.CharField(db_column='TxnType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salescount = models.IntegerField(db_column='SalesCount')  # Field name made lowercase.
    cardstatus = models.SmallIntegerField(db_column='CardStatus', blank=True, null=True)  # Field name made lowercase.
    cardid = models.CharField(db_column='CardID', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cardpercent = models.DecimalField(db_column='CardPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalcardpoint = models.DecimalField(db_column='TotalCardPoint', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatincluded = models.CharField(db_column='VATIncluded', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    vatpercent = models.DecimalField(db_column='VATPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesbonustype = models.CharField(db_column='SalesBonusType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salesbonuspercent = models.DecimalField(db_column='SalesBonusPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesbonusamount = models.DecimalField(db_column='SalesBonusAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesdiscounttype = models.CharField(db_column='SalesDiscountType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salesdiscountpercent = models.DecimalField(db_column='SalesDiscountPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesdiscountamount = models.DecimalField(db_column='SalesDiscountAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalsalesamount = models.DecimalField(db_column='TotalSalesAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalvatamount = models.DecimalField(db_column='TotalVATAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalsoldamount = models.DecimalField(db_column='TotalSoldAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalbonusamount = models.DecimalField(db_column='TotalBonusAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totaldiscountamount = models.DecimalField(db_column='TotalDiscountAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalcardamount = models.DecimalField(db_column='TotalCardAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totaldueamount = models.DecimalField(db_column='TotalDueAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalpaidamount = models.DecimalField(db_column='TotalPaidAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalcashamount = models.DecimalField(db_column='TotalCashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalnoncashamount = models.DecimalField(db_column='TotalNonCashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    refno = models.CharField(db_column='RefNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descr = models.CharField(db_column='Descr', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    summaryupdated = models.SmallIntegerField(db_column='SummaryUpdated', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    postingid = models.BigIntegerField(db_column='PostingID', blank=True, null=True)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    sicount = models.SmallIntegerField(db_column='SICount', blank=True, null=True)  # Field name made lowercase.
    picount = models.SmallIntegerField(db_column='PICount', blank=True, null=True)  # Field name made lowercase.
    periodyear = models.IntegerField(db_column='PeriodYear', blank=True, null=True)  # Field name made lowercase.
    totalpdsalesamount = models.DecimalField(db_column='TotalPdSalesAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalpricedownamount = models.DecimalField(db_column='TotalPriceDownAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalnhat = models.DecimalField(db_column='TotalNHAT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    custcpnyid = models.CharField(db_column='CustCpnyID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    custcpnyname = models.CharField(db_column='CustCpnyName', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ddtdno = models.CharField(db_column='DDTDNo', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccorder = models.CharField(db_column='ccOrder', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psSales_0510'


class Pssetup(models.Model):
    cpnyid = models.CharField(db_column='CpnyID', primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    basecurrencyid = models.CharField(db_column='BaseCurrencyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    vatpercent = models.DecimalField(db_column='VATPercent', max_digits=19, decimal_places=4)  # Field name made lowercase.
    decplacesqty = models.SmallIntegerField(db_column='DecPlacesQty')  # Field name made lowercase.
    decplacescostprice = models.SmallIntegerField(db_column='DecPlacesCostPrice')  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'psSetup'


class Psshopsafecashout(models.Model):
    cashoutid = models.CharField(db_column='CashOutID', primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    siteid = models.CharField(db_column='SiteID', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    outdate = models.CharField(db_column='OutDate', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    outtime = models.CharField(db_column='OutTime', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    outtype = models.CharField(db_column='OutType', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    outbank = models.CharField(db_column='OutBank', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    outempcode = models.CharField(db_column='OutEmpCode', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    outamount = models.DecimalField(db_column='OutAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'psShopSafeCashOut'


class Pssummarytmp(models.Model):
    siteid = models.CharField(db_column='SiteID', primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (SiteID, InvtID, PeriodY, PeriodM) found, that is not supported. The first column is selected.
    invtid = models.CharField(db_column='InvtID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    periody = models.SmallIntegerField(db_column='PeriodY')  # Field name made lowercase.
    periodm = models.SmallIntegerField(db_column='PeriodM')  # Field name made lowercase.
    sq01 = models.DecimalField(db_column='SQ01', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq01 = models.DecimalField(db_column='RQ01', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq02 = models.DecimalField(db_column='SQ02', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq02 = models.DecimalField(db_column='RQ02', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq03 = models.DecimalField(db_column='SQ03', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq03 = models.DecimalField(db_column='RQ03', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq04 = models.DecimalField(db_column='SQ04', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq04 = models.DecimalField(db_column='RQ04', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq05 = models.DecimalField(db_column='SQ05', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq05 = models.DecimalField(db_column='RQ05', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq06 = models.DecimalField(db_column='SQ06', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq06 = models.DecimalField(db_column='RQ06', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq07 = models.DecimalField(db_column='SQ07', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq07 = models.DecimalField(db_column='RQ07', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq08 = models.DecimalField(db_column='SQ08', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq08 = models.DecimalField(db_column='RQ08', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq09 = models.DecimalField(db_column='SQ09', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq09 = models.DecimalField(db_column='RQ09', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq10 = models.DecimalField(db_column='SQ10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq10 = models.DecimalField(db_column='RQ10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq11 = models.DecimalField(db_column='SQ11', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq11 = models.DecimalField(db_column='RQ11', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq12 = models.DecimalField(db_column='SQ12', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq12 = models.DecimalField(db_column='RQ12', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq13 = models.DecimalField(db_column='SQ13', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq13 = models.DecimalField(db_column='RQ13', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq14 = models.DecimalField(db_column='SQ14', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq14 = models.DecimalField(db_column='RQ14', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq15 = models.DecimalField(db_column='SQ15', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq15 = models.DecimalField(db_column='RQ15', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq16 = models.DecimalField(db_column='SQ16', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq16 = models.DecimalField(db_column='RQ16', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq17 = models.DecimalField(db_column='SQ17', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq17 = models.DecimalField(db_column='RQ17', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq18 = models.DecimalField(db_column='SQ18', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq18 = models.DecimalField(db_column='RQ18', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq19 = models.DecimalField(db_column='SQ19', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq19 = models.DecimalField(db_column='RQ19', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq20 = models.DecimalField(db_column='SQ20', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq20 = models.DecimalField(db_column='RQ20', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq21 = models.DecimalField(db_column='SQ21', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq21 = models.DecimalField(db_column='RQ21', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq22 = models.DecimalField(db_column='SQ22', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq22 = models.DecimalField(db_column='RQ22', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq23 = models.DecimalField(db_column='SQ23', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq23 = models.DecimalField(db_column='RQ23', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq24 = models.DecimalField(db_column='SQ24', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq24 = models.DecimalField(db_column='RQ24', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq25 = models.DecimalField(db_column='SQ25', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq25 = models.DecimalField(db_column='RQ25', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq26 = models.DecimalField(db_column='SQ26', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq26 = models.DecimalField(db_column='RQ26', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq27 = models.DecimalField(db_column='SQ27', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq27 = models.DecimalField(db_column='RQ27', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq28 = models.DecimalField(db_column='SQ28', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq28 = models.DecimalField(db_column='RQ28', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq29 = models.DecimalField(db_column='SQ29', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq29 = models.DecimalField(db_column='RQ29', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq30 = models.DecimalField(db_column='SQ30', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq30 = models.DecimalField(db_column='RQ30', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sq31 = models.DecimalField(db_column='SQ31', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rq31 = models.DecimalField(db_column='RQ31', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa01 = models.DecimalField(db_column='SA01', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra01 = models.DecimalField(db_column='RA01', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa02 = models.DecimalField(db_column='SA02', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra02 = models.DecimalField(db_column='RA02', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa03 = models.DecimalField(db_column='SA03', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra03 = models.DecimalField(db_column='RA03', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa04 = models.DecimalField(db_column='SA04', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra04 = models.DecimalField(db_column='RA04', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa05 = models.DecimalField(db_column='SA05', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra05 = models.DecimalField(db_column='RA05', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa06 = models.DecimalField(db_column='SA06', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra06 = models.DecimalField(db_column='RA06', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa07 = models.DecimalField(db_column='SA07', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra07 = models.DecimalField(db_column='RA07', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa08 = models.DecimalField(db_column='SA08', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra08 = models.DecimalField(db_column='RA08', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa09 = models.DecimalField(db_column='SA09', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra09 = models.DecimalField(db_column='RA09', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa10 = models.DecimalField(db_column='SA10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra10 = models.DecimalField(db_column='RA10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa11 = models.DecimalField(db_column='SA11', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra11 = models.DecimalField(db_column='RA11', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa12 = models.DecimalField(db_column='SA12', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra12 = models.DecimalField(db_column='RA12', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa13 = models.DecimalField(db_column='SA13', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra13 = models.DecimalField(db_column='RA13', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa14 = models.DecimalField(db_column='SA14', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra14 = models.DecimalField(db_column='RA14', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa15 = models.DecimalField(db_column='SA15', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra15 = models.DecimalField(db_column='RA15', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa16 = models.DecimalField(db_column='SA16', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra16 = models.DecimalField(db_column='RA16', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa17 = models.DecimalField(db_column='SA17', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra17 = models.DecimalField(db_column='RA17', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa18 = models.DecimalField(db_column='SA18', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra18 = models.DecimalField(db_column='RA18', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa19 = models.DecimalField(db_column='SA19', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra19 = models.DecimalField(db_column='RA19', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa20 = models.DecimalField(db_column='SA20', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra20 = models.DecimalField(db_column='RA20', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa21 = models.DecimalField(db_column='SA21', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra21 = models.DecimalField(db_column='RA21', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa22 = models.DecimalField(db_column='SA22', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra22 = models.DecimalField(db_column='RA22', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa23 = models.DecimalField(db_column='SA23', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra23 = models.DecimalField(db_column='RA23', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa24 = models.DecimalField(db_column='SA24', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra24 = models.DecimalField(db_column='RA24', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa25 = models.DecimalField(db_column='SA25', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra25 = models.DecimalField(db_column='RA25', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa26 = models.DecimalField(db_column='SA26', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra26 = models.DecimalField(db_column='RA26', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa27 = models.DecimalField(db_column='SA27', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra27 = models.DecimalField(db_column='RA27', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa28 = models.DecimalField(db_column='SA28', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra28 = models.DecimalField(db_column='RA28', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa29 = models.DecimalField(db_column='SA29', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra29 = models.DecimalField(db_column='RA29', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa30 = models.DecimalField(db_column='SA30', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra30 = models.DecimalField(db_column='RA30', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sa31 = models.DecimalField(db_column='SA31', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ra31 = models.DecimalField(db_column='RA31', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psSummaryTmp'
        unique_together = (('siteid', 'invtid', 'periody', 'periodm'),)


class Psterminalbalance(models.Model):
    terminalid = models.CharField(db_column='TerminalID', primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (TerminalID, PeriodDate, CashierEmpCode, CurrencyID) found, that is not supported. The first column is selected.
    perioddate = models.CharField(db_column='PeriodDate', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cashierempcode = models.CharField(db_column='CashierEmpCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    currencyid = models.CharField(db_column='CurrencyID', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    openingamount = models.DecimalField(db_column='OpeningAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    salesamount = models.DecimalField(db_column='SalesAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    incomeamount = models.DecimalField(db_column='IncomeAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    returnamount = models.DecimalField(db_column='ReturnAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    expenseamount = models.DecimalField(db_column='ExpenseAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    closingamount = models.DecimalField(db_column='ClosingAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'psTerminalBalance'
        unique_together = (('terminalid', 'perioddate', 'cashierempcode', 'currencyid'),)


class Psterminalbalancedtl(models.Model):
    terminalid = models.CharField(db_column='TerminalID', primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (TerminalID, PeriodDate, CashierEmpCode, CurrencyID, Type, BillID) found, that is not supported. The first column is selected.
    perioddate = models.CharField(db_column='PeriodDate', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cashierempcode = models.CharField(db_column='CashierEmpCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    currencyid = models.CharField(db_column='CurrencyID', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    billid = models.IntegerField(db_column='BillID')  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    qty = models.IntegerField(db_column='Qty')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'psTerminalBalanceDtl'
        unique_together = (('terminalid', 'perioddate', 'cashierempcode', 'currencyid', 'type', 'billid'),)


class Psterminalcashier(models.Model):
    terminalid = models.CharField(db_column='TerminalID', primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (TerminalID, PeriodDate, CashierEmpCode) found, that is not supported. The first column is selected.
    perioddate = models.CharField(db_column='PeriodDate', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cashierempcode = models.CharField(db_column='CashierEmpCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    openingbalentered = models.SmallIntegerField(db_column='OpeningBalEntered', blank=True, null=True)  # Field name made lowercase.
    closingbalentered = models.SmallIntegerField(db_column='ClosingBalEntered', blank=True, null=True)  # Field name made lowercase.
    lasttxndate = models.CharField(db_column='LastTxnDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lasttxntype = models.CharField(db_column='LastTxnType', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lasttxnno = models.CharField(db_column='LastTxnNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'psTerminalCashier'
        unique_together = (('terminalid', 'perioddate', 'cashierempcode'),)


class Psterminalinfo(models.Model):
    terminalid = models.CharField(db_column='TerminalID', primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (TerminalID, PeriodDate) found, that is not supported. The first column is selected.
    perioddate = models.CharField(db_column='PeriodDate', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    islocked = models.SmallIntegerField(db_column='IsLocked')  # Field name made lowercase.
    timeofbod = models.CharField(db_column='TimeOfBOD', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    timeofeod = models.CharField(db_column='TimeOfEOD', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salescount = models.IntegerField(db_column='SalesCount')  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.
    totalsalescount = models.IntegerField(db_column='TotalSalesCount', blank=True, null=True)  # Field name made lowercase.
    totalsalesitemcount = models.IntegerField(db_column='TotalSalesItemCount', blank=True, null=True)  # Field name made lowercase.
    totalpaymentitemcount = models.IntegerField(db_column='TotalPaymentItemCount', blank=True, null=True)  # Field name made lowercase.
    posversion = models.CharField(db_column='PosVersion', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psTerminalInfo'
        unique_together = (('terminalid', 'perioddate'),)


class PsSalebarcode(models.Model):
    recid = models.BigIntegerField(db_column='RecID', primary_key=True)  # Field name made lowercase.
    txncostid = models.BigIntegerField(db_column='TxnCostID')  # Field name made lowercase.
    invtid = models.CharField(db_column='InvtID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    siteid = models.CharField(db_column='SiteID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    unitid = models.CharField(db_column='UnitID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    barcode = models.CharField(db_column='BarCode', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=19, decimal_places=4)  # Field name made lowercase.
    startdate = models.CharField(db_column='StartDate', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    expiredate = models.CharField(db_column='ExpireDate', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    saleprice = models.DecimalField(db_column='SalePrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    printquantity = models.IntegerField(db_column='PrintQuantity', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=300, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    printeddate = models.CharField(db_column='PrintedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    printedusername = models.CharField(db_column='PrintedUserName', max_length=300, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=300, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ps_SaleBarCode'


class Rbproductorder(models.Model):
    orderno = models.CharField(db_column='OrderNo', primary_key=True, max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txnempcode = models.CharField(db_column='TxnEmpCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txndate = models.CharField(db_column='TxnDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    branchid = models.CharField(db_column='BranchID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    hallid = models.CharField(db_column='HallID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    roomid = models.CharField(db_column='RoomID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tableid = models.CharField(db_column='TableID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    terminalid = models.CharField(db_column='TerminalID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    descr = models.CharField(db_column='Descr', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    oldstatus = models.SmallIntegerField(db_column='OldStatus', blank=True, null=True)  # Field name made lowercase.
    totalunitqty = models.DecimalField(db_column='TotalUnitQty', max_digits=19, decimal_places=4)  # Field name made lowercase.
    totalunitamt = models.DecimalField(db_column='TotalUnitAmt', max_digits=19, decimal_places=4)  # Field name made lowercase.
    sourceno = models.CharField(db_column='SourceNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cardstatus = models.SmallIntegerField(db_column='CardStatus', blank=True, null=True)  # Field name made lowercase.
    cardid = models.CharField(db_column='CardID', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cardpercent = models.DecimalField(db_column='CardPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    voiddate = models.CharField(db_column='VoidDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    voidempcode = models.CharField(db_column='VoidEmpCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    voiddescr = models.CharField(db_column='VoidDescr', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'rbProductOrder'


class Rbproductorderitem(models.Model):
    productid = models.CharField(db_column='ProductID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    orderno = models.CharField(db_column='OrderNo', primary_key=True, max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (OrderNo, ProductID, UnitID) found, that is not supported. The first column is selected.
    unitid = models.CharField(db_column='UnitID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    unitqty = models.DecimalField(db_column='UnitQty', max_digits=19, decimal_places=4)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4)  # Field name made lowercase.
    unittotalamt = models.DecimalField(db_column='UnitTotalAmt', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemstatus = models.SmallIntegerField(db_column='ItemStatus')  # Field name made lowercase.
    itemreason = models.CharField(db_column='ItemReason', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'rbProductOrderItem'
        unique_together = (('orderno', 'productid', 'unitid'),)


class Rbsales(models.Model):
    salesno = models.CharField(db_column='SalesNo', primary_key=True, max_length=24, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    branchid = models.CharField(db_column='BranchID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    hallid = models.CharField(db_column='HallID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    roomid = models.CharField(db_column='RoomID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tableid = models.CharField(db_column='TableID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    terminalid = models.CharField(db_column='TerminalID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txndate = models.CharField(db_column='TxnDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    txnempcode = models.CharField(db_column='TxnEmpCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salesdate = models.CharField(db_column='SalesDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cardstatus = models.SmallIntegerField(db_column='CardStatus', blank=True, null=True)  # Field name made lowercase.
    cardid = models.CharField(db_column='CardID', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cardpercent = models.DecimalField(db_column='CardPercent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalsalesamount = models.DecimalField(db_column='TotalSalesAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalcardamount = models.DecimalField(db_column='TotalCardAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totaldueamount = models.DecimalField(db_column='TotalDueAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalpaidamount = models.DecimalField(db_column='TotalPaidAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalcashamount = models.DecimalField(db_column='TotalCashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalnoncashamount = models.DecimalField(db_column='TotalNonCashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    postingid = models.BigIntegerField(db_column='PostingID', blank=True, null=True)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'rbSales'


class Rbsalesitem(models.Model):
    salesno = models.CharField(db_column='SalesNo', primary_key=True, max_length=24, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (SalesNo, LineNbr) found, that is not supported. The first column is selected.
    linenbr = models.SmallIntegerField(db_column='LineNbr')  # Field name made lowercase.
    cpnyid = models.CharField(db_column='CpnyID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salesdate = models.CharField(db_column='SalesDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    productid = models.CharField(db_column='ProductID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    unitid = models.CharField(db_column='UnitID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemsalesprice = models.DecimalField(db_column='ItemSalesPrice', max_digits=19, decimal_places=4)  # Field name made lowercase.
    itemsoldamount = models.DecimalField(db_column='ItemSoldAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    createdprogid = models.CharField(db_column='CreatedProgID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdusername = models.CharField(db_column='CreatedUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LastUpdate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastusername = models.CharField(db_column='LastUserName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tstamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'rbSalesItem'
        unique_together = (('salesno', 'linenbr'),)


class Sysarticlecolumns(models.Model):
    artid = models.IntegerField()
    colid = models.IntegerField()
    is_udt = models.BooleanField(blank=True, null=True)
    is_xml = models.BooleanField(blank=True, null=True)
    is_max = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysarticlecolumns'
        unique_together = (('artid', 'colid'),)


class Sysarticles(models.Model):
    artid = models.AutoField()
    creation_script = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    del_cmd = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dest_table = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    filter = models.IntegerField()
    filter_clause = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    ins_cmd = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    name = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    objid = models.IntegerField()
    pubid = models.IntegerField()
    pre_creation_cmd = models.SmallIntegerField()
    status = models.SmallIntegerField()
    sync_objid = models.IntegerField()
    type = models.SmallIntegerField()
    upd_cmd = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    schema_option = models.TextField(blank=True, null=True)  # This field type is a guess.
    dest_owner = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    ins_scripting_proc = models.IntegerField(blank=True, null=True)
    del_scripting_proc = models.IntegerField(blank=True, null=True)
    upd_scripting_proc = models.IntegerField(blank=True, null=True)
    custom_script = models.CharField(max_length=2048, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    fire_triggers_on_snapshot = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'sysarticles'
        unique_together = (('artid', 'pubid'),)


class Sysarticleupdates(models.Model):
    artid = models.IntegerField()
    pubid = models.IntegerField()
    sync_ins_proc = models.IntegerField()
    sync_upd_proc = models.IntegerField()
    sync_del_proc = models.IntegerField()
    autogen = models.BooleanField()
    sync_upd_trig = models.IntegerField()
    conflict_tableid = models.IntegerField(blank=True, null=True)
    ins_conflict_proc = models.IntegerField(blank=True, null=True)
    identity_support = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'sysarticleupdates'
        unique_together = (('artid', 'pubid'),)


class Syspublications(models.Model):
    description = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    name = models.CharField(unique=True, max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    pubid = models.AutoField(unique=True)
    repl_freq = models.SmallIntegerField()
    status = models.SmallIntegerField()
    sync_method = models.SmallIntegerField()
    snapshot_jobid = models.TextField(blank=True, null=True)  # This field type is a guess.
    independent_agent = models.BooleanField()
    immediate_sync = models.BooleanField()
    enabled_for_internet = models.BooleanField()
    allow_push = models.BooleanField()
    allow_pull = models.BooleanField()
    allow_anonymous = models.BooleanField()
    immediate_sync_ready = models.BooleanField()
    allow_sync_tran = models.BooleanField()
    autogen_sync_procs = models.BooleanField()
    retention = models.IntegerField(blank=True, null=True)
    allow_queued_tran = models.BooleanField()
    snapshot_in_defaultfolder = models.BooleanField()
    alt_snapshot_folder = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    pre_snapshot_script = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    post_snapshot_script = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    compress_snapshot = models.BooleanField()
    ftp_address = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    ftp_port = models.IntegerField()
    ftp_subdirectory = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    ftp_login = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    ftp_password = models.CharField(max_length=524, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    allow_dts = models.BooleanField()
    allow_subscription_copy = models.BooleanField()
    centralized_conflicts = models.BooleanField(blank=True, null=True)
    conflict_retention = models.IntegerField(blank=True, null=True)
    conflict_policy = models.IntegerField(blank=True, null=True)
    queue_type = models.IntegerField(blank=True, null=True)
    ad_guidname = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    backward_comp_level = models.IntegerField()
    allow_initialize_from_backup = models.BooleanField()
    min_autonosync_lsn = models.TextField(blank=True, null=True)  # This field type is a guess.
    replicate_ddl = models.IntegerField(blank=True, null=True)
    options = models.IntegerField()
    originator_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'syspublications'


class Sysreplservers(models.Model):
    srvname = models.CharField(primary_key=True, max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    srvid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysreplservers'


class Sysschemaarticles(models.Model):
    artid = models.IntegerField()
    creation_script = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dest_object = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    objid = models.IntegerField()
    pubid = models.IntegerField()
    pre_creation_cmd = models.SmallIntegerField()
    status = models.IntegerField()
    type = models.SmallIntegerField()
    schema_option = models.TextField(blank=True, null=True)  # This field type is a guess.
    dest_owner = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysschemaarticles'
        unique_together = (('artid', 'pubid'),)


class Syssubscriptions(models.Model):
    artid = models.IntegerField()
    srvid = models.SmallIntegerField()
    dest_db = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    status = models.SmallIntegerField()
    sync_type = models.SmallIntegerField()
    login_name = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    subscription_type = models.IntegerField()
    distribution_jobid = models.TextField(blank=True, null=True)  # This field type is a guess.
    timestamp = models.TextField()  # This field type is a guess.
    update_mode = models.SmallIntegerField()
    loopback_detection = models.BooleanField()
    queued_reinit = models.BooleanField()
    nosync_type = models.SmallIntegerField()
    srvname = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'syssubscriptions'
        unique_together = (('artid', 'srvid', 'dest_db', 'srvname'),)


class Systranschemas(models.Model):
    tabid = models.IntegerField()
    startlsn = models.TextField(unique=True)  # This field type is a guess.
    endlsn = models.TextField()  # This field type is a guess.
    typeid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'systranschemas'


class Test(models.Model):
    testxml = models.TextField(db_column='testXML', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test'


class Tmpxml(models.Model):
    xmlvalues = models.TextField(db_column='XMLValues', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpXML'
