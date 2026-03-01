from rest_framework import serializers
from market_app.models import Market, Product, Seller


class MarketSerializer(serializers.ModelSerializer):

    sellers = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Market
        # fields = '__all__'
        # fields = ['name','location','description','net_worth']
        exclude = ['name']


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
        fields = ['id','name','contact_info','market_count', 'markets', 'market_ids']

    def get_market_count(self, obj):
        return obj.markets.count()