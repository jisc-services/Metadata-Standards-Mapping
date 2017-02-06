
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

Use the casrai:Author Name:, casrai:Author ID: and possibly casrai:Author ID Type: to construct an identifier for the rioxx:Author: field, for example the following values:

    Author ID: http://orcid.org/0000-0002-1395-3092
    Author Name: Lawson, Gerald
    Author ID Type: Person ID Types/ORCID

would map to the following rioxx:author: field:

    <rioxxterms:author id="http://orcid.org/0000-0002-1395-3092">
        Lawson, Gerald
    </rioxxterms:author>

# casrai-app_author_id_type-rioxx-author

Use the casrai:Author Name:, casrai:Author ID: and possibly casrai:Author ID Type: to construct an identifier for the rioxx:Author: field, for example the following values:

    Author ID: http://orcid.org/0000-0002-1395-3092
    Author Name: Lawson, Gerald
    Author ID Type: Person ID Types/ORCID

would map to the following rioxx:author: field:

    <rioxxterms:author id="http://orcid.org/0000-0002-1395-3092">
        Lawson, Gerald
    </rioxxterms:author>

# casrai-app_author_name-rioxx-author

Use the casrai:Author Name:, casrai:Author ID: and possibly casrai:Author ID Type: to construct an identifier for the rioxx:Author: field, for example the following values:

    Author_ID: http://orcid.org/0000-0002-1395-3092
    Author_Name: Lawson, Gerald
    Author_ID_Type: Person ID Types/ORCID

would map to the following rioxx:author: field:

    <rioxxterms:author id="http://orcid.org/0000-0002-1395-3092">
        Lawson, Gerald
    </rioxxterms:author>

# hefce-embargo_end_date-openaire-access_level

Use hefce:embargo_end_date to infer whether the openaire:access_level is ```openAccess``` (embargo has expired) or ```embargoedAccess```(embargo still in force).

## Examples

    <ali:free_to_read>
'
maps to:

    <dc:rights>info:eu-repo/semantics/openAccess</dc:rights>

    Embargo_End_Date: 2020-04-13

maps to:

    <dc:rights>info:eu-repo/semantics/embargoedAccess</dc:rights>

# hefce-embargo_end_date-rioxx-free_to_read

Use hefce:embargo_end_date to infer whether the resource is rioxx:free_to_read.

## Examples

    <ali:free_to_read>
'
maps to:

    <ali:free_to_read>

    Embargo_End_Date: 2013-01-29

maps to:

    <ali:free_to_read>

# hefce-free_to_read-openaire-access_level

The ````info:eu-repo/semantics/openAccess``` openaire:access_level can be determined from the hefce:free_to_read element (if the resource is not Open Access it is not possible to determine its access level from hefce:free_to_read alone).

## Examples:

    <ali:free_to_read>
    <ali:free_to_read start_date="2013-03-28">

Both hefce:free_to_read values map to:

    <dc:rights>info:eu-repo/semantics/openAccess</dc:rights>

But the following value (or the absence of a value) results in no mapping:

    <ali:free_to_read start_date="2013-03-28" end_date="2014-04-30">

# hefce-license_ref-casrai-apc_licence_type

Use pattern matching to identify Creative Commons licenses and map them to the appropriate casrai:apc_license_type.

## Examples

The following hefce:license_ref value:

    <ali:license_ref>http://creativecommons.org/licenses/by/4.0</ali:license_ref>

maps to:

    Licence Types/CC BY

[casrai:apc_license_type dictionary](http://dictionary.casrai.org/Licence_Types)

# hefce-version_of_deposited_file-openaire-publication_version

Map the hefce:version_of_deposited_file value to the appropriate openaire:publication_version:

| AO | draft |
| SMUR | submittedVersion |
| AM | acceptedVersion |
| P | no mapping |
| VoR | publishedVersion |
| CVoR | updatedVersion |
| EVoR | updatedVersion |
| NA | no mapping |

## Examples

   <rioxxterms:version>AM</rioxxterms:version>

maps to:

    <dc:type>info:eu-repo/semantics/acceptedVersion</dc:type>

# openaire-access_level-hefce-free_to_read

If the <span class="schema-element schema-element-openaire">Access Level</span> is ```openAccess```, set <span class="schema-element schema-element-hefce">Free to Read</span>, for example:

    <dc:rights>info:eu-repo/semantics/openAccess</dc:rights>

maps to:

    <ali:free_to_read>

# openaire-access_level-rioxx-free_to_read

If the <span class="schema-element schema-element-openaire">Access Level</span> is ```openAccess```, set <span class="schema-element schema-element-rioxx">Free to Read</span>, for example:

    <dc:rights>info:eu-repo/semantics/openAccess</dc:rights>

maps to:

    <ali:free_to_read>

# openaire-alternative_identifier-casrai-ja_issn

If the <span class="schema-element schema-element-openaire">Alternative Identifier</span> element has a ```eissn``` or ```pissn``` scheme, map it to the <span class="schema-element schema-element-casrai">ISSN</span> element, for example:

    <dc:relation>
        info:eu-repo/semantics/altIdentifier/pissn/0028-0836
    </dc:relation>

maps to:

     0028-0836

# openaire-alternative_identifier-casrai-ja_pmc_id

If the <span class="schema-element schema-element-openaire">Alternative Identifier</span> element has a ```pmid``` scheme, map it to the <span class="schema-element schema-element-casrai">PMC ID</span> element, for example:

    <dc:relation>
        info:eu-repo/semantics/altIdentifier/pmid/27819666
    </dc:relation>

maps to:

    27819666

# openaire-embargo_end_date-hefce-free_to_read

If the <span class="schema-element schema-element-openaire">Embargo End Date</span> has passed, set <span class="schema-element schema-element-hefce">Free to Read</span>, for example:

    <dc:date>info:eu-repo/date/embargoEnd/2015-12-31</dc:date>

maps to:

    <ali:free_to_read start_date="2015-12-31">

# openaire-embargo_end_date-rioxx-free_to_read

If the <span class="schema-element schema-element-openaire">Embargo End Date</span> has passed, set <span class="schema-element schema-element-rioxx">Free to Read</span>, for example:

    <dc:date>info:eu-repo/date/embargoEnd/2015-12-31</dc:date>

maps to:

    <ali:free_to_read start_date="2015-12-31">

# openaire-license_condition-casrai-apc_licence_type

Apply pattern matching to the <span class="schema-element schema-element-openaire">License Condition</span> element to try and extract a corresponding CLicence TypeC, for example:

    <dc:rights>http://creativecommons.org/licenses/by-sa/2.0/uk/</dc:rights>

    <dc:rights>cc-by-sa, Andrew Smith</dc:rights>

    <dc:rights>cc-by-sa, info:eu-repo/dai/nl/344568</dc:rights>

all map to:

    <span class="schema-element schema-element-casrai"></span> BY-SA    

See list of allowable <span class="schema-element schema-element-casrai">License Type</span> values; http://dictionary.casrai.org/Licence_Types

# openaire-license_condition-hefce-license_ref

If the <span class="schema-element schema-element-openaire">License Condition</span> is a HTTP URI (or a HTTP URI can be derived) map it to <span class="schema-element schema-element-hefce">License Ref</span>, for example:

    <dc:rights>
        http://creativecommons.org/licenses/by-sa/2.0/uk/
    </dc:rights>

maps to:

    <ali:license_ref start_date="2015-02-17">
        http://creativecommons.org/licenses/by-sa/2.0/uk/
    </ali:license_ref>

and:

    <dc:rights>cc-by-sa, Andrew Smith</dc:rights>

maps to (note CC 4.0 assumed):

    <ali:license_ref start_date="2015-02-17">
        http://creativecommons.org/licenses/by-sa/4.0<
    /ali:license_ref>

Note that ```start_date``` must be included, for example use the date the mapping took place.

# openaire-license_condition-rioxx-license_ref

If the <span class="schema-element schema-element-openaire">License Condition</span> is a HTTP URI (or a HTTP URI can be derived) map it to <span class="schema-element schema-element-rioxx">License Ref</span>, for example:

    <dc:rights>
        http://creativecommons.org/licenses/by-sa/2.0/uk/
    </dc:rights>

maps to:

    <ali:license_ref start_date="2015-02-17">
        http://creativecommons.org/licenses/by-sa/2.0/uk/
    </ali:license_ref>

and:

    <dc:rights>cc-by-sa, Andrew Smith</dc:rights>

maps to (note CC 4.0 assumed):

    <ali:license_ref start_date="2015-02-17">
        http://creativecommons.org/licenses/by-sa/4.0<
    /ali:license_ref>

Note that ```start_date``` must be included, for example use the date the mapping took place.

# openaire-project_identifier-casrai-apc_source_grants

Extract the ```ProjectID``` from the <span class="schema-element schema-element-openaire">Project Identifier</span> URI, for example:

    <dc:relation>
        info:eu-repo/grantAgreement/ARC/Future Fellowships/FT120100464
    </dc:relation>

maps to:

    FT120100464 

# openaire-project_identifier-rioxx-project

Extract the ```Funder``` and ```ProjectID``` from the <span class="schema-element schema-element-openaire">Project Identifier</span> URI, for example:

    <dc:relation>
        info:eu-repo/grantAgreement/ARC/Future Fellowships/FT120100464
    </dc:relation>

maps to:

    <rioxxterms:project funder_name="ARC">
       FT120100464 
    </rioxxterms:project>

# openaire-publication_version-hefce-version_of_deposited_file

Map the <span class="schema-element schema-element-openaire">Publication Version</span> vocabulary to the <span class="schema-element schema-element-hefce">Version</span> vocabulary:

| draft | AO |
| submittedVersion | SMUR |
| acceptedVersion | AM |
| publishedVersion | VoR |
| updatedVersion | CVoR |

For example:

    <dc:type>info:eu-repo/semantics/acceptedVersion</dc:type>

maps to:

    <rioxxterms:version>AM</rioxxterms:version>


# openaire-publication_version-rioxx-version

Map the <span class="schema-element schema-element-openaire">Publication Version</span> vocabulary to the <span class="schema-element schema-element-rioxx">Version</span> vocabulary:

| draft | AO |
| submittedVersion | SMUR |
| acceptedVersion | AM |
| publishedVersion | VoR |
| updatedVersion | CVoR |

For example:

    <dc:type>info:eu-repo/semantics/acceptedVersion</dc:type>

maps to:

    <rioxxterms:version>AM</rioxxterms:version>

# openaire-resource_identifier-casrai-ja_doi

If one of the <span class="schema-element schema-element-openaire">Resource Identifier</span> values contains a DOI, map it to CDOIC, for example:

    <dc:identifier>http://hdl.handle.net/1234/5628 </dc:identifier>
    <dc:identifier>urn:isbn:123456789</dc:identifier>
    <dc:identifier>info:doi:10-123456789</dc:identifier>

maps to:

    10-123456789

# openaire-resource_identifier-casrai-ja_issn

If one of the <span class="schema-element schema-element-openaire">Resource Identifier</span> values contains an ISSN, map it to CISSNC, for example:

    <dc:identifier>http://hdl.handle.net/1234/5628 </dc:identifier>
    <dc:identifier>urn:issn:0028-0836</dc:identifier>
    <dc:identifier>info:doi:10-123456789</dc:identifier>

maps to:

    0028-0836

# openaire-resource_identifier-casrai-ja_pmc_id

If one of the <span class="schema-element schema-element-openaire">Resource Identifier</span> values contains a Pubmed URL, map it to <span class="schema-element schema-element-casrai">PM</span> IDC, for example:

    <dc:identifier>
        https://www.ncbi.nlm.nih.gov/pubmed/27818134
    </dc:identifier>
    <dc:identifier>urn:issn:0028-0836</dc:identifier>
    <dc:identifier>info:doi:10-123456789</dc:identifier>

maps to:

    27818134

# openaire-resource_identifier-rioxx-version_of_record

If one of the <span class="schema-element schema-element-openaire">Resource Identifier</span> values contains a DOI, map it to <span class="schema-element schema-element-rioxx">Version of Record</span>, for example:

    <dc:identifier>http://hdl.handle.net/1234/5628 </dc:identifier>
    <dc:identifier>urn:isbn:123456789</dc:identifier>
    <dc:identifier>info:doi:10.1006/jmbi.1995.0238</dc:identifier>

maps to:

    <rioxxterms:version_of_record>
        http://dx.doi.org/10.1006/jmbi.1995.0238
    </rioxxterms:version_of_record>

Note that the DOI must be represented in its HTTP form.

# rioxx-apc-casrai-apc_payment_adjustments

Map the rioxx:APC: vocabulary value to a suitable string in casrai:Payment Adjustments:, for eexample: 

    <rioxxterms:apc>
        partially waived
    </rioxxterms:apc>

could be mapped to:

    "Partially waived"

or:

    "APC cost partially waived by publisher"

# rioxx-author-casrai-app_author_id

Extract the casrai:Author ID: value from the rioxx:Author field, for example:

    <rioxxterms:author id="http://orcid.org/0000-0002-1395-3092">
        Lawson, Gerald
    </rioxxterms:author>

produces:

    http://orcid.org/0000-0002-1395-3092

# rioxx-author-casrai-app_author_id_type

Use pattern matching to recognise an ORCID or ISNI in the rioxx:Author: field, for example:

    <rioxxterms:author id="http://orcid.org/0000-0002-1395-3092">
        Lawson, Gerald
    </rioxxterms:author>

would identify the casrai:Author ID Type: as:

    Person ID Types/ORCID

See http://dictionary.casrai.org/Person_ID_Types for

# rioxx-author-casrai-app_author_name

Extract the casrai:Author Name: value from the rioxx:Author: field, for example:

    <rioxxterms:author id="http://orcid.org/0000-0002-1395-3092">
        Lawson, Gerald
    </rioxxterms:author>

produces:

    Lawson, Gerald

# rioxx-author-openaire-creator

Extract the openaire:Creator: value from the rioxx:Author: field, for example:

    <rioxxterms:author id="http://orcid.org/0000-0002-1395-3092">
        Lawson, Gerald
    </rioxxterms:author>

produces:

    <dc:creator>
        Lawson, Gerald
    </dc:creator>

# rioxx-free_to_read-openaire-access_level

The ````info:eu-repo/semantics/openAccess``` openaire:access_level can be determined from the rioxx:free_to_read element (if the resource is not Open Access it is not possible to determine its access level from rioxx:free_to_read alone).

    <license_

## Examples:

    <ali:free_to_read>
    <ali:free_to_read start_date="2013-03-28">

Both rioxx:free_to_read values map to:

    <dc:rights>info:eu-repo/semantics/openAccess</dc:rights>

But the following value (or the absence of a value) results in no mapping:

    <ali:free_to_read start_date="2013-03-28" end_date="2014-04-30">

# rioxx-license_ref-casrai-apc_licence_type

Use pattern matching to identify Creative Commons licenses and map them to the appropriate casrai:apc_license_type.

## Examples

The following rioxx:license_ref value:

    <ali:license_ref>http://creativecommons.org/licenses/by/4.0</ali:license_ref>

maps to:

    Licence Types/CC BY

[casrai:apc_license_type dictionary](http://dictionary.casrai.org/Licence_Types)


# rioxx-project-casrai-apc_source_grants

Extract the project ID from the rioxx:project value.

## Examples

    <rioxxterms:project
        funder_name="Engineering and Physical Sciences Research Council"
        funder_id="http://isni.org/isni/0000000403948681"
    >
        EP/K023195/1
    </rioxxterms:project>

maps to:

    APC_Payment/Source_Grant(s): EP/K023195/1

# rioxx-project-openaire-project_identifier

Extract the ```funder_name``` and project ID from the rioxx:project element to create a partial ```info:eu-repo/grantAgreement``` identifier. Use the [OpenAire list of projects](http://api.openaire.eu/oai_pmh?verb=ListRecords&set=projects&metadataPrefix=oaf) to verify the project details.

## Examples

    <rioxxterms:project
        funder_name="Engineering and Physical Sciences Research Council"
        funder_id="http://isni.org/isni/0000000403948681"
    >
        EP/K023195/1
    </rioxxterms:project>

maps to:

    <dc:relation>
        info:eu-repo/grantAgreement/EPSRC//EP%2FK023195%2F1///
    </dc:relation>

# rioxx-version_of_record-casrai-ja_doi

Use pattern matching to determine if the rioxx:version_of_record is a DOI and if so, map it to casrai:ja_doi.

## Examples

    <rioxxterms:version_of_record>
        http://dx.doi.org/10.1006/jmbi.1995.0238
    </rioxxterms:version_of_record>

maps to:

    Journal_Article/DOI: http://dx.doi.org/10.1006/jmbi.1995.0238

# rioxx-version-openaire-publication_version

Map the rioxx:version value to the appropriate openaire:publication_version:

| AO | draft |
| SMUR | submittedVersion |
| AM | acceptedVersion |
| P | no mapping |
| VoR | publishedVersion |
| CVoR | updatedVersion |
| EVoR | updatedVersion |
| NA | no mapping |

## Examples

   <rioxxterms:version>AM</rioxxterms:version>

maps to:

    <dc:type>info:eu-repo/semantics/acceptedVersion</dc:type>
