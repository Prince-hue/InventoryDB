# Generated by Django 4.2.6 on 2023-12-24 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InOut', '0002_asset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='name_of_asset',
            field=models.CharField(choices=[('Cup Brush 4"', 'Cup Brush 4"'), ('Cup Brush 3"', 'Cup Brush 3"'), ('Paint Brush 2"', 'Paint Brush 2"'), ('Paint Brush 3"', 'Paint Brush 3"'), ('Paint Brush 4"', 'Paint Brush 4"'), ('Paint Brush 6"', 'Paint Brush 6"'), ('Angle Brush 2"', 'Angle Brush 2"'), ('Angle Brush 3"', 'Angle Brush 3"'), ('Angle Brush 4"', 'Angle Brush 4"'), ('Rolling Brush 2"', 'Rolling Brush 2"'), ('Rolling Brush 4"', 'Rolling Brush 4"'), ('Rolling Brush 9"', 'Rolling Brush 9"'), ('Wire brush (Plastic type)', 'Wire brush (Plastic type)'), ('Non spark cap wire brush 3"', 'Non spark cap wire brush 3"'), ('Abrasive fibre disc', 'Abrasive fibre disc'), ('Non Spark Wire Brush', 'Non Spark Wire Brush'), ('Chipping Hammer', 'Chipping Hammer'), ('Esab Electrode 7018 (2.5) x 350 mm - packets', 'Esab Electrode 7018 (2.5) x 350 mm - packets'), ('Esab Electrode 7018 (2.5) x 450 mm - packets', 'Esab Electrode 7018 (2.5) x 450 mm - packets'), ('Pittsburg Paint', 'Pittsburg Paint'), ('PPG Thinner', 'PPG Thinner'), ('Gasket 16" - 150# 316 B16 - 20 Klinger - SBM - Spiral wound', 'Gasket 16" - 150# 316 B16 - 20 Klinger - SBM - Spiral wound'), ('Gasket 16" - 150# Fibre NAF Gasket - SBM ', 'Gasket 16" - 150# Fibre NAF Gasket - SBM '), ('Gasket 16" - 300# Type - Ring Stainless Steel - SBM - Spiral wound', 'Gasket 16" - 300# Type - Ring Stainless Steel - SBM - Spiral wound'), ('Gasket 20" - 150# Klinger 316 L - SBM Spiral wound', 'Gasket 20" - 150# Klinger 316 L - SBM Spiral wound'), ('Gasket 20" - 300# LBS B16 20 P005003 - SBM Spiral wound', 'Gasket 20" - 300# LBS B16 20 P005003 - SBM Spiral wound'), ('5500D x 450ID x 3mm Thick Gasket 60 Shore', '5500D x 450ID x 3mm Thick Gasket 60 Shore'), ('6500D x 550ID x 3mm Thick Gasket 60 Shore', '6500D x 550ID x 3mm Thick Gasket 60 Shore'), ('1200D x 95ID x 4mm Thick Gasket 60 Shore', '1200D x 95ID x 4mm Thick Gasket 60 Shore'), ('18" Gasket 150# Spiral wound', '18" Gasket 150# Spiral wound'), ('Ring Gasket (RTJ) - 16"', 'Ring Gasket (RTJ) - 16"'), ('Ring Gasket (RTJ) - 12"', 'Ring Gasket (RTJ) - 12"'), ('2" 150# Spiral wound Gasket', '2" 150# Spiral wound Gasket'), ('333 75 Seal (Pig Switch)', '333 75 Seal (Pig Switch)'), ('322 75 Seal (Pig Switch)', '322 75 Seal (Pig Switch)'), ('60mm Seal (Pig Switch)', '60mm Seal (Pig Switch)'), ('70mm Seal (Pig Switch)', '70mm Seal (Pig Switch)'), ('12" O - Ring', '12" O - Ring'), ('Ball valve 4" 300Ib 1set gasket', 'Ball valve 4" 300Ib 1set gasket'), ('Ball valve 6" 300Ib 1set gasket', 'Ball valve 6" 300Ib 1set gasket'), ('Gate valve 8" 150Ib 1set gasket', 'Gate valve 8" 150Ib 1set gasket'), ('Gate valve 8" 300Ib 1set gasket', 'Gate valve 8" 300Ib 1set gasket'), ('Gate valve 12" 150Ib 1set gasket ', 'Gate valve 12" 150Ib 1set gasket '), ('Gate valve 12" 300Ib 1set gasket', 'Gate valve 12" 300Ib 1set gasket'), ('Gate valve 18" 300Ib 1set gasket', 'Gate valve 18" 300Ib 1set gasket'), ('Irabounc UU55/52A', 'Irabounc UU55/52A'), ('Molykote', 'Molykote'), ('Belzona Cleaner Degreaser', 'Belzona Cleaner Degreaser'), ('Belzona 1212 Base', 'Belzona 1212 Base'), ('Belzona Soldifier', 'Belzona Soldifier'), ('Belzona 8411', 'Belzona 8411'), ('Belzona 1161 Base', 'Belzona 1161 Base'), ('Rap Tape', 'Rap Tape'), ('C.F Tape', 'C.F Tape'), ('EPDM', 'EPDM'), ('Dove saw and other saw', 'Dove saw and other saw'), ('Green Heart Wood', 'Green Heart Wood'), ('QRH keeper', 'QRH keeper'), ('Cable shoes', 'Cable shoes'), ('Cable connector ', 'Cable connector '), ('M12 bolts with washers', 'M12 bolts with washers'), ('Chain Block 5 ton - Able', 'Chain Block 5 ton - Able'), ('Chain Block 3 ton Atlas', 'Chain Block 3 ton Atlas'), ('Yalelift 360 manual chanin Hoist 3000 kg', 'Yalelift 360 manual chanin Hoist 3000 kg'), ('Yalelift 360 manual chanin Hoist 2000 kg', 'Yalelift 360 manual chanin Hoist 2000 kg'), ('Yalelift 360 manual chanin Hoist 1000 kg', 'Yalelift 360 manual chanin Hoist 1000 kg'), ('Lightweight oil industry snatch block shackle head 2 tonnes / 7 - 9 mm', 'Lightweight oil industry snatch block shackle head 2 tonnes / 7 - 9 mm'), ('Bravo Lever Hoist 3 ton', 'Bravo Lever Hoist 3 ton'), ('Bravo Lever Hoist 1.5 ton', 'Bravo Lever Hoist 1.5 ton'), ('12T G2130OC Bolt Type Anchor Shackle 1 - 1/4" Maxtough ', '12T G2130OC Bolt Type Anchor Shackle 1 - 1/4" Maxtough '), ('17T G2130OC 17T OC Bolt Type Anchor Shackle 1 - 1/2" Maxtough', '17T G2130OC 17T OC Bolt Type Anchor Shackle 1 - 1/2" Maxtough'), ('35T G2130OC 35t OC Bolt Type Anchor Shackle 2" Maxtough', '35T G2130OC 35t OC Bolt Type Anchor Shackle 2" Maxtough'), ('8.5T G2130OC 8.5T OC Bolt Type Anchor Shackle 1" Maxtough', '8.5T G2130OC 8.5T OC Bolt Type Anchor Shackle 1" Maxtough'), ('9.5T G2130OC 8.5T OC BOLT TYPE ANCHOR', '9.5T G2130OC 8.5T OC BOLT TYPE ANCHOR'), ('SHACKLE 1- 1/8" MAXTOUGH and Van Beest (2)', 'SHACKLE 1- 1/8" MAXTOUGH and Van Beest (2)'), ('6.5T G2130OC OC Bolt Type Anchor Shackle 7/8"', '6.5T G2130OC OC Bolt Type Anchor Shackle 7/8"'), ('Maxtough and Van Beest (2)', 'Maxtough and Van Beest (2)'), ('12t Van beest Screw pin', '12t Van beest Screw pin'), ('3.25T G-4163, Green Pin Bow Shackle BN, Standard bow shackle with safety bolt to EN13889, Hot ', '3.25T G-4163, Green Pin Bow Shackle BN, Standard bow shackle with safety bolt to EN13889, Hot ')], max_length=255),
        ),
    ]
