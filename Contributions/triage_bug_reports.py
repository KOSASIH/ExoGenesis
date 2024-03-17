def triage_bug_reports(bug_reports):
    """
    Triage bug reports submitted by users or contributors, prioritizing them for resolution based on severity and impact.

    :param bug_reports: A list of bug reports, where each report is a dictionary containing keys for 'severity', 'priority', and 'impact'.
    :return: A list of triaged bug reports, sorted by priority.
    """

    # Calculate the priority score for each bug report
    for report in bug_reports:
        priority_score = report['severity'] * report['priority'] * report['impact']
        report['priority_score'] = priority_score

    # Sort the bug reports by priority score in descending order
    triaged_bug_reports = sorted(bug_reports, key=lambda report: report['priority_score'], reverse=True)

    return triaged_bug_reports
