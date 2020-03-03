from loaders.wiki_loader import WikiLoader

def get_loader(args):
    """get_loader
    :param name:
    """
    return {
        'wiki_crop' : WikiLoader,
        # feel free to add new datasets here
    }[args.dataset]