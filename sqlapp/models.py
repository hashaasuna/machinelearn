from django.db import models

# Create your models here.
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
        db_table = 'psTerminalInfo'
        unique_together = (('terminalid', 'perioddate'),)

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

from django.db import models

# Create your models here.
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
        db_table = 'psTerminalInfo'
        unique_together = (('terminalid', 'perioddate'),)

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