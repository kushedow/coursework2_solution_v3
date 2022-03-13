import pytest

from classes.comments_dao import CommentsDAO

from classes.posts_dao import PostsDAO


@pytest.fixture
def comments_dao():
    return CommentsDAO("data/comments.json")

@pytest.fixture
def posts_dao():
    return PostsDAO("data/data.json")

