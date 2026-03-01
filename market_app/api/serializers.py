from rest_framework import serializers
from market_app.models import Market, Product, Seller


class MarketSerializer(serializers.HyperlinkedModelSerializer):
    sellers = serializers.StringRelatedField(many=True, read_only=True)
    # sellers = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='seller_single')

    class Meta:
        model = Market
        fields = '__all__'
        # fields = ['id', 'name','location','description','net_worth','sellers','url']
        # exclude = ['name']


class MarketHyperlinkedSerializer(MarketSerializer, serializers.HyperlinkedModelSerializer):

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    # sellers = None
    class Meta:
        model = Market
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):

    markets = MarketSerializer(many=True, read_only=True)
    market_ids = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all(),
        many=True,
        write_only=True,
        source='markets'
    )
    market_count = serializers.SerializerMethodField()

    class Meta:
        model = Seller
        fields = ['id', 'name', 'contact_info',
                  'market_count', 'markets', 'market_ids']

    def get_market_count(self, obj):
        return obj.markets.count()
