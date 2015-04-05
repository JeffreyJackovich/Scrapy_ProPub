BOT_NAME = 'propub'

SPIDER_MODULES = ['propub.spiders']
NEWSPIDER_MODULE = 'propub.spiders'
ITEM_PIPELINES = ['propub.pipelines.PropubPipeline']
