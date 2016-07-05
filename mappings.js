$('#get-data').click(function () {
    $.getJSON('data.json', function (data) {

        var schemas = []; // schemas[schema] = {}
        var fields = []; // fields[schema][field] = {}
        var mappings = []; // mappings[schema][field] = {}

        // init lookups
        for (var i=0, slen=data.schemas.length; i < slen; i++) {
            schema = data.schemas[i];
            schemas[schema.id] = schema;
            fields[schema.id] = [];
            mappings[schema.id] = [];
            for (var j=0, flen=schema.fields.length; j < flen; j++) {
                field = schema.fields[j];
                if(field.mappings) {
                    var field_mappings = [];
                    for (var k=0, mlen=field.mappings.length; k < mlen; k++) {
                        var mapping = field.mappings[k];
                        field_mappings[mapping.schema] = mapping;
                    }
                    mappings[schema.id][field.id] = field_mappings;
                }
            }
        }

        var cols = ["rioxx", "openaire"];
        var selected_schema = schemas[cols[0]];

        for (var i=0, len=selected_schema.fields.length; i < len; i++) {
            field = selected_schema.fields[i];
            console.log(field.label);
        }
    });
});
