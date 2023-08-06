from unittest import TestCase
from blog_tool.tags import Tags


class TagsTest(TestCase):
    def test_tags(self):
        # Given:
        input = "tags: [\"東京女子プロレス\",\"Notion\",\"Spotify\"]"

        # When:
        tags = Tags.from_string(input)
        print(tags.values)

        # Then:
        expected = ["Spotify", "Notion", "東京女子プロレス"]
        self.assertEqual(sorted(expected), sorted(tags.values))
