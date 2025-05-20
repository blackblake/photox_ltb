from rest_framework import serializers
from .models import Image

# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Image
#         fields=['id', 'image_url', 'title', 'tags', 'user', 'created_at','is_public','category_id', 'colors']

class ImageUploadSerializer(serializers.Serializer):
    image=serializers.ImageField()
    title = serializers.CharField(required=False, max_length=255)
    is_public = serializers.BooleanField(required=False, default=False)

class ImageSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()  # 用于返回类别名称

    class Meta:
        model = Image
        fields = ['id', 'image_url', 'title', 'tags', 'user', 'created_at', 'is_public', 'category_id', 'category', 'colors']

    def get_category(self, obj):
        category_map = {
            0: "风景", 1: "人物肖像", 2: "动物", 3: "交通工具", 4: "食品",
            5: "建筑", 6: "电子产品", 7: "运动器材", 8: "植物花卉", 9: "医疗用品",
            10: "办公用品", 11: "服装鞋帽", 12: "家具家居", 13: "书籍文档", 14: "艺术创作",
            15: "工业设备", 16: "体育赛事", 17: "天文地理", 18: "儿童玩具", 19: "美妆个护",
            20: "军事装备", 21: "宠物用品", 22: "健身器材", 23: "厨房用品", 24: "实验室器材",
            25: "音乐器材", 26: "户外装备", 27: "珠宝首饰", 28: "虚拟场景", 29: "其他"
        }
        return category_map.get(obj.category_id, "未知")

