import unittest


from Models.schema import AgentSchema, ETLAgentSchema, RouterSchema


class SchemaTests(unittest.TestCase):
    def test_agent_schema_provides_empty_message_list(self):
        schema = AgentSchema(
            user_question="What is the dataset?",
            curated_ques="",
            prompt_query_context="",
            generated_sql_query="",
            is_safe="No",
            comments="",
            sql_query_execution_result="",
            final_answer="",
        )

        self.assertEqual(schema.messages, [])

    def test_etl_schema_provides_empty_message_list(self):
        schema = ETLAgentSchema()

        self.assertEqual(schema.messages, [])

    def test_router_schema_accepts_valid_route(self):
        schema = RouterSchema(answer="sql", comments="Looks like a SQL request")

        self.assertEqual(schema.answer, "sql")


if __name__ == "__main__":
    unittest.main()
