from django.test import TestCase

from openforms.forms.tests.factories import FormFactory, FormStepFactory

from ...form_logic import evaluate_form_logic
from ..factories import SubmissionFactory, SubmissionStepFactory
from .factories import FormLogicFactory


class ComponentModificationTests(TestCase):
    def test_change_component_to_hidden(self):
        form = FormFactory.create()
        step1 = FormStepFactory.create(
            form=form,
            form_definition__configuration={
                "components": [
                    {
                        "type": "textfield",
                        "key": "step1_textfield1",
                    }
                ]
            },
        )
        step2 = FormStepFactory.create(
            form=form,
            form_definition__configuration={
                "components": [
                    {
                        "type": "textfield",
                        "key": "step2_textfield1",
                        "hidden": False,
                    }
                ]
            },
        )
        FormLogicFactory.create(
            form=form,
            json_logic_trigger={
                "==": [
                    {"var": "step1_textfield1"},
                    "hide step 2",
                ]
            },
            actions=[
                {
                    "component": "step2_textfield1",
                    "action": {
                        "name": "Hide element",
                        "type": "property",
                        "property": {
                            "value": "hidden",
                        },
                        "state": True,
                    },
                }
            ],
        )
        submission = SubmissionFactory.create(form=form)
        SubmissionStepFactory.create(
            submission=submission,
            form_step=step1,
            data={"step1_textfield1": "hide step 2"},
        )
        # not saved in DB!
        submission_step_2 = SubmissionStepFactory.build(
            submission=submission,
            form_step=step2,
        )

        configuration = evaluate_form_logic(submission_step_2, submission.data)

        expected = {
            "components": [
                {
                    "type": "textfield",
                    "key": "step2_textfield1",
                    "hidden": True,
                }
            ]
        }
        self.assertEqual(configuration, expected)

    def test_extract_value(self):
        form = FormFactory.create()
        step1 = FormStepFactory.create(
            form=form,
            form_definition__configuration={
                "components": [
                    {
                        "type": "textfield",
                        "key": "step1_textfield1",
                    }
                ]
            },
        )
        step2 = FormStepFactory.create(
            form=form,
            form_definition__configuration={
                "components": [
                    {
                        "type": "textfield",
                        "key": "step2_textfield1",
                        "hidden": False,
                    }
                ]
            },
        )
        FormLogicFactory.create(
            form=form,
            json_logic_trigger={"==": [1, 1]},
            actions=[
                {
                    "component": "step2_textfield1",
                    "action": {
                        "name": "Set extracted value",
                        "type": "value",
                        "value": {"var": "step1_textfield1"},
                    },
                }
            ],
        )
        submission = SubmissionFactory.create(form=form)
        SubmissionStepFactory.create(
            submission=submission,
            form_step=step1,
            data={"step1_textfield1": "some value"},
        )
        # not saved in DB!
        submission_step_2 = SubmissionStepFactory.build(
            submission=submission,
            form_step=step2,
        )

        configuration = evaluate_form_logic(submission_step_2, submission.data)

        expected = {
            "components": [
                {
                    "type": "textfield",
                    "key": "step2_textfield1",
                    "hidden": False,
                    "value": "some value",
                }
            ]
        }
        self.assertEqual(configuration, expected)


class StepModificationTests(TestCase):
    def test_next_button_disabled(self):
        form = FormFactory.create()
        step1 = FormStepFactory.create(
            form=form,
            form_definition__configuration={
                "components": [
                    {
                        "type": "textfield",
                        "key": "step1_textfield1",
                    }
                ]
            },
        )
        step2 = FormStepFactory.create(
            form=form,
            form_definition__configuration={
                "components": [
                    {
                        "type": "textfield",
                        "key": "step2_textfield1",
                    }
                ]
            },
        )
        FormLogicFactory.create(
            form=form,
            json_logic_trigger={
                "==": [
                    {"var": "step1_textfield1"},
                    "disable next button",
                ]
            },
            actions=[
                {
                    "component": "step2_textfield1",
                    "action": {
                        "name": "Hide element",
                        "type": "disable-next",
                    },
                }
            ],
        )
        submission = SubmissionFactory.create(form=form)
        SubmissionStepFactory.create(
            submission=submission,
            form_step=step1,
            data={"step1_textfield1": "disable next button"},
        )
        # not saved in DB!
        submission_step_2 = SubmissionStepFactory.build(
            submission=submission,
            form_step=step2,
        )

        self.assertTrue(submission_step_2.can_submit)

        evaluate_form_logic(submission_step_2, submission.data)

        self.assertFalse(submission_step_2.can_submit)