
# casrai-apc_licence_type-hefce-license_ref

See list of allowable <span class="schema-element schema-element-casrai">License Type</span> values; http://dictionary.casrai.org/Licence_Types

The License Type value can be converted to a Creative Commons URL, for example:

    Licence Types/CC BY-NC-ND

can be mapped to:

    http://creativecommons.org/licenses/by-nc-nd/4.0/

in the <span class="schema-element schema-element-hefce">License Ref</span> field.

# casrai-apc_licence_type-openaire-license_condition

See list of allowable <span class="schema-element schema-element-casrai">License Type</span> values; http://dictionary.casrai.org/Licence_Types

The License Type value can be converted to a Creative Commons URL, for example:

    Licence Types/CC BY-NC-ND

can be mapped to:

    <dc:rights>
        http://creativecommons.org/licenses/by-nc-nd/4.0/
    </dc:rights>

in the <span class="schema-element schema-element-openaire">License Condition</span> field.

# casrai-apc_licence_type-rioxx-license_ref

See list of allowable <span class="schema-element schema-element-casrai">License Type</span> values; http://dictionary.casrai.org/Licence_Types

The License Type value can be converted to a Creative Commons URL, for example:

    Licence Types/CC BY-NC-ND

can be mapped to:

    <ali:license_ref start_date="2016-06-05">
        http://creativecommons.org/licenses/by-nc-nd/4.0/
    </ali:license_ref>

in the <span class="schema-element schema-element-rioxx">License Ref</span> field. Note that a ```start_date``` must be included - in the absence of any other data this could be the date that the mapping took place.

# casrai-apc_payment_adjustments-rioxx-apc

The <span class="schema-element schema-element-casrai">Payment Adjustments</span> value may be able to be converted to one of the allowable <span class="schema-element schema-element-rioxx">APC</span> values, for example:

    "The APC cost was partially waived by the publisher"

could, perhaps using automated pattern matching, feasibly be mapped to:

    <rioxxterms:apc>
        partially waived
    </rioxxterms:apc>

# casrai-apc_source_grants-openaire-project_identifier

The <span class="schema-element schema-element-casrai">Source Grant(s)</span> value can be used to build an OpenAire compliant [Grant Agreement identifier](https://wiki.surfnet.nl/display/standards/info-eu-repo#info-eu-repo-GrantAgreementIdentifiers) suitable for the <span class="schema-element schema-element-openaire">Project Identifier</span> field, for example:

    FT120100464

could, perhaps via an [authority list](http://api.openaire.eu/oai_pmh?verb=ListRecords&set=projects&metadataPrefix=oaf), be mapped to:

    <dc:relation>
        info:eu-repo/grantAgreement/ARC/Future Fellowships/FT120100464
    </dc:relation>

# casrai-apc_source_funds-rioxx-project

The <span class="schema-element schema-element-casrai">Source Fund(s)</span> and <span class="schema-element schema-element-casrai">Source Grants(s)</span> values could be combined and mapped to the <span class="schema-element schema-element-rioxx">Project</span> field, for example:

    Source Fund(s): ARC
    Source Grant(s): FT120100464

could be combined into:

    <rioxxterms:project
        funder_name="ARC">
        FT120100464
    </rioxxterms:project>

# casrai-apc_source_grants-rioxx-project

The <span class="schema-element schema-element-casrai">Source Fund(s)</span> and <span class="schema-element schema-element-casrai">Source Grants(s)</span> values could be combined and mapped to the <span class="schema-element schema-element-rioxx">Project</span> field, for example:

    Source Fund(s): ARC
    Source Grant(s): FT120100464

could be combined into:

    <rioxxterms:project
        funder_name="ARC">
        FT120100464
    </rioxxterms:project>

# casrai-app_author_id-rioxx-author

Build HTTP URI

# casrai-app_author_id_type-rioxx-author

Build HTTP URI

# casrai-app_author_name-rioxx-author

Name part only

# hefce-embargo_end_date-openaire-access_level

Set to embargoedAccess or openAccess (assuming open access after embargo ends)

# hefce-embargo_end_date-rioxx-free_to_read

Assuming free to read after embargo ends

# hefce-free_to_read-openaire-access_level

Set Access Level to openAccess if within start/end dates

# hefce-license_ref-casrai-apc_licence_type

With vocab mapping

# hefce-version_of_deposited_file-openaire-publication_version

With vocabulary mapping

# openaire-access_level-hefce-free_to_read

If Access Level is openAccess

# openaire-access_level-rioxx-free_to_read

If Access Level is openAccess

# openaire-alternative_identifier-casrai-ja_issn

If Alternative Identifier scheme is eissn or pissn

# openaire-alternative_identifier-casrai-ja_pmc_id

If Alternative Identifier scheme is pmid

# openaire-creator-casrai-app_author_id

Derive from HTTP URI

# openaire-creator-casrai-app_author_id_type

Derive from HTTP URI

# openaire-creator-casrai-app_author_name

Name part only

# openaire-creator-rioxx-author

Name part only

# openaire-embargo_end_date-hefce-free_to_read

Assuming free to read after embargo ends

# openaire-embargo_end_date-rioxx-free_to_read

Assuming free to read after embargo ends

# openaire-license_condition-casrai-apc_licence_type

Convert string to vocab

# openaire-license_condition-hefce-license_ref

If License Condition is CC

# openaire-license_condition-rioxx-license_ref

If License Condition is CC

# openaire-project_identifier-casrai-apc_source_grants

Map ProjectID

# openaire-project_identifier-rioxx-project

Map Funder to funder_name and ProjectID to project ID

# openaire-publication_version-hefce-version_of_deposited_file

With vocabulary mapping

# openaire-publication_version-rioxx-version

With vocabulary mapping

# openaire-resource_identifier-casrai-ja_doi

If Resource Identifier includes a DOI URL

# openaire-resource_identifier-casrai-ja_issn

If Resource Identifier includes a ISSN URL

# openaire-resource_identifier-casrai-ja_pmc_id

If Resource Identifier includes a PMID URL

# openaire-resource_identifier-rioxx-version_of_record

If Resource Identifier includes a DOI URL (or ISSN/ISBN?)

# rioxx-apc-casrai-apc_payment_adjustments

Convert vocab to string

# rioxx-author-casrai-app_author_id

Derive from HTTP URI

# rioxx-author-casrai-app_author_id_type

Derive from HTTP URI

# rioxx-author-casrai-app_author_name

Name part only

# rioxx-author-openaire-creator

Name part only

# rioxx-free_to_read-openaire-access_level

The presence of an ali:free_to_read element can be used to infer that Open Access to the resource is possible, provided that the end_date attribute is not a date in the past.

# rioxx-license_ref-casrai-apc_licence_type

With vocab mapping

# rioxx-project-casrai-apc_source_grants

Map project ID

# rioxx-project-openaire-project_identifier

Map funder_name to Funder and project ID to ProjectID

# rioxx-version_of_record-casrai-ja_doi

Applies only if VoR value is a DOI

# rioxx-version-openaire-publication_version

With vocabulary mapping
