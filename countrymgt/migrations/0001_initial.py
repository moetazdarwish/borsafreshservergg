# Generated by Django 4.0 on 2022-06-18 17:24

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountryManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('shipping', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('shipping_flat', models.BooleanField(blank=True, default=True, null=True)),
                ('tax_rate', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('tax', models.BooleanField(blank=True, default=True, null=True)),
                ('symbl', models.CharField(blank=True, max_length=5, null=True)),
                ('approved', models.BooleanField(blank=True, default=False, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CountryUserConst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secolag', models.CharField(blank=True, max_length=50, null=True)),
                ('tediprf', models.CharField(blank=True, max_length=150, null=True)),
                ('tediprf_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('tmrkcov', models.CharField(blank=True, max_length=150, null=True)),
                ('tmrkcov_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('tfruts', models.CharField(blank=True, max_length=150, null=True)),
                ('tfruts_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('thrblf', models.CharField(blank=True, max_length=150, null=True)),
                ('thrblf_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('thydro', models.CharField(blank=True, max_length=150, null=True)),
                ('thydro_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('tmfrtb', models.CharField(blank=True, max_length=150, null=True)),
                ('tmfrtb_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('tmvgeb', models.CharField(blank=True, max_length=150, null=True)),
                ('tmvgeb_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('tmshrm', models.CharField(blank=True, max_length=150, null=True)),
                ('tmshrm_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('taddnte', models.CharField(blank=True, max_length=150, null=True)),
                ('taddnte_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('tprflt', models.CharField(blank=True, max_length=150, null=True)),
                ('tprflt_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('tcart', models.CharField(blank=True, max_length=150, null=True)),
                ('tcart_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('tcartls', models.CharField(blank=True, max_length=150, null=True)),
                ('tcartls_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('tfaq', models.CharField(blank=True, max_length=150, null=True)),
                ('tfaq_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('tsprt', models.CharField(blank=True, max_length=150, null=True)),
                ('tsprt_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('bprfsve', models.CharField(blank=True, max_length=150, null=True)),
                ('bprfsve_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('bprfedte', models.CharField(blank=True, max_length=150, null=True)),
                ('bprfedte_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('bpay', models.CharField(blank=True, max_length=150, null=True)),
                ('bpay_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('bnte', models.CharField(blank=True, max_length=150, null=True)),
                ('bnte_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('bgnrl', models.CharField(blank=True, max_length=150, null=True)),
                ('bgnrl_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('bdlry', models.CharField(blank=True, max_length=150, null=True)),
                ('bdlry_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('brtun', models.CharField(blank=True, max_length=150, null=True)),
                ('brtun_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('bbck', models.CharField(blank=True, max_length=150, null=True)),
                ('bbck_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('bvegts', models.CharField(blank=True, max_length=150, null=True)),
                ('bvegts_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('sprfphn', models.CharField(blank=True, max_length=150, null=True)),
                ('sprfphn_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('sprfcde', models.CharField(blank=True, max_length=150, null=True)),
                ('sprfcde_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('sprfare', models.CharField(blank=True, max_length=150, null=True)),
                ('sprfare_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('sprfadd', models.CharField(blank=True, max_length=150, null=True)),
                ('sprfadd_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('sqty', models.CharField(blank=True, max_length=150, null=True)),
                ('sqty_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('snte', models.CharField(blank=True, max_length=150, null=True)),
                ('snte_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('sphne', models.CharField(blank=True, max_length=150, null=True)),
                ('sphne_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('sadrs', models.CharField(blank=True, max_length=150, null=True)),
                ('sadrs_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('sptcde', models.CharField(blank=True, max_length=150, null=True)),
                ('sptcde_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('sarea', models.CharField(blank=True, max_length=150, null=True)),
                ('sarea_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('scty', models.CharField(blank=True, max_length=150, null=True)),
                ('scty_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('scntry', models.CharField(blank=True, max_length=150, null=True)),
                ('scntry_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('sabtol', models.CharField(blank=True, max_length=150, null=True)),
                ('sabtol_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('ssping', models.CharField(blank=True, max_length=150, null=True)),
                ('ssping_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('stvat', models.CharField(blank=True, max_length=150, null=True)),
                ('stvat_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('stolt', models.CharField(blank=True, max_length=150, null=True)),
                ('stolt_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('sgtdtls', models.CharField(blank=True, max_length=150, null=True)),
                ('sgtdtls_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('sitprc', models.CharField(blank=True, max_length=150, null=True)),
                ('sitprc_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('country', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='countrymgt.countrymanager')),
            ],
        ),
        migrations.CreateModel(
            name='CountryAppConst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secolag', models.CharField(blank=True, max_length=50, null=True)),
                ('d_addproduct', models.CharField(blank=True, max_length=50, null=True)),
                ('d_addproduct_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('d_alloffers', models.CharField(blank=True, max_length=50, null=True)),
                ('d_alloffers_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('d_orders', models.CharField(blank=True, max_length=50, null=True)),
                ('d_orders_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('d_account', models.CharField(blank=True, max_length=50, null=True)),
                ('d_account_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('d_support', models.CharField(blank=True, max_length=50, null=True)),
                ('d_support_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('d_faq', models.CharField(blank=True, max_length=50, null=True)),
                ('d_faq_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('f_vegetables', models.CharField(blank=True, max_length=50, null=True)),
                ('f_vegetables_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('f_fruits', models.CharField(blank=True, max_length=50, null=True)),
                ('f_fruits_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('f_herbsleaf', models.CharField(blank=True, max_length=50, null=True)),
                ('f_herbsleaf_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('f_mushroom', models.CharField(blank=True, max_length=50, null=True)),
                ('f_mushroom_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('f_mixbox', models.CharField(blank=True, max_length=50, null=True)),
                ('f_mixbox_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('f_accall', models.CharField(blank=True, max_length=50, null=True)),
                ('f_accall_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('f_accpaid', models.CharField(blank=True, max_length=50, null=True)),
                ('f_accpaid_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('f_ordnew', models.CharField(blank=True, max_length=50, null=True)),
                ('f_ordnew_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('f_ordproc', models.CharField(blank=True, max_length=50, null=True)),
                ('f_ordproc_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('f_ordall', models.CharField(blank=True, max_length=50, null=True)),
                ('f_ordall_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('f_faqgen', models.CharField(blank=True, max_length=50, null=True)),
                ('f_faqgen_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('f_faqpol', models.CharField(blank=True, max_length=50, null=True)),
                ('f_faqpol_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('titfaq', models.CharField(blank=True, max_length=50, null=True)),
                ('titfaq_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('titacc', models.CharField(blank=True, max_length=50, null=True)),
                ('titacc_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('titord', models.CharField(blank=True, max_length=50, null=True)),
                ('titord_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('titoff', models.CharField(blank=True, max_length=50, null=True)),
                ('titoff_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('titbxd', models.CharField(blank=True, max_length=50, null=True)),
                ('titbxd_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('titdlt', models.CharField(blank=True, max_length=50, null=True)),
                ('titdlt_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('titmkt', models.CharField(blank=True, max_length=50, null=True)),
                ('titmkt_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('titrev', models.CharField(blank=True, max_length=50, null=True)),
                ('titrev_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('titait', models.CharField(blank=True, max_length=50, null=True)),
                ('titait_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('titsof', models.CharField(blank=True, max_length=50, null=True)),
                ('titsof_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('titcmb', models.CharField(blank=True, max_length=50, null=True)),
                ('titcmb_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('titodt', models.CharField(blank=True, max_length=50, null=True)),
                ('titodt_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('titnor', models.CharField(blank=True, max_length=50, null=True)),
                ('titnor_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('scrtot', models.CharField(blank=True, max_length=50, null=True)),
                ('scrtot_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('scrref', models.CharField(blank=True, max_length=50, null=True)),
                ('scrref_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('scrqty', models.CharField(blank=True, max_length=50, null=True)),
                ('scrqty_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('scrprc', models.CharField(blank=True, max_length=50, null=True)),
                ('scrprc_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('scrstk', models.CharField(blank=True, max_length=50, null=True)),
                ('scrstk_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('scrdue', models.CharField(blank=True, max_length=50, null=True)),
                ('scrdue_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('scrnme', models.CharField(blank=True, max_length=50, null=True)),
                ('scrnme_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('scrphn', models.CharField(blank=True, max_length=50, null=True)),
                ('scrphn_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('scrkg', models.CharField(blank=True, max_length=50, null=True)),
                ('scrkg_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('scrbch', models.CharField(blank=True, max_length=50, null=True)),
                ('scrbch_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('scradd', models.CharField(blank=True, max_length=50, null=True)),
                ('scradd_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('scrv1d', models.CharField(blank=True, max_length=50, null=True)),
                ('scrv1d_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('scrv2d', models.CharField(blank=True, max_length=50, null=True)),
                ('scrv2d_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('scrv3d', models.CharField(blank=True, max_length=50, null=True)),
                ('scrv3d_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('scrvbx', models.CharField(blank=True, max_length=50, null=True)),
                ('scrvbx_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('scrfbx', models.CharField(blank=True, max_length=50, null=True)),
                ('scrfbx_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('scradss', models.CharField(blank=True, max_length=50, null=True)),
                ('scradss_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('scrara', models.CharField(blank=True, max_length=50, null=True)),
                ('scrara_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('scrrjt', models.CharField(blank=True, max_length=50, null=True)),
                ('scrrjt_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('scracp', models.CharField(blank=True, max_length=50, null=True)),
                ('scracp_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('scrdlv', models.CharField(blank=True, max_length=50, null=True)),
                ('scrdlv_sl', models.CharField(blank=True, max_length=50, null=True)),
                ('accbnk', models.CharField(blank=True, max_length=150, null=True)),
                ('accbnk_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('sbtncg', models.CharField(blank=True, max_length=150, null=True)),
                ('sbtncg_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('shtbk', models.CharField(blank=True, max_length=150, null=True)),
                ('shtbk_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('tbank', models.CharField(blank=True, max_length=150, null=True)),
                ('tbank_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('scrpce', models.CharField(blank=True, max_length=150, null=True)),
                ('scrpce_sl', models.CharField(blank=True, max_length=150, null=True)),
                ('country', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='countrymgt.countrymanager')),
            ],
        ),
        migrations.CreateModel(
            name='CityManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('trader_percent', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('farm_percent', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('custommer_percent', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('shipping', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('shipping_flat', models.BooleanField(blank=True, default=True, null=True)),
                ('approved', models.BooleanField(blank=True, default=False, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='countrymgt.countrymanager')),
            ],
        ),
    ]
