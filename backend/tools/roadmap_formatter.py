class RoadmapFormatter:

    @staticmethod
    def sort_weeks(roadmap: list):

        return sorted(
            roadmap,
            key=lambda x: x["week"],
        )