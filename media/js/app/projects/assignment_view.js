/* global _: true, Backbone: true, MediaThread: true, showMessage: true */

/**
 * Listens For:
 * Nothing
 *
 * Signals:
 * Nothing
 */

(function(jQuery) {
    var global = this;

    global.AssignmentView = Backbone.View.extend({
        events: {
            'click .submit-response': 'onSubmitResponse',
            'click .btn-show-submit': 'onShowSubmitDialog',
            'click .toggle-feedback': 'onToggleFeedback',
            'click .save-feedback': 'onSaveFeedback'
        },
        initialize: function(options) {
            var self = this;
            self.viewer = options.viewer;
            self.isFaculty = options.isFaculty;
            self.feedback = options.feedback;
            self.feedbackCount = options.feedbackCount;
            self.myResponse = parseInt(options.responseId, 10);

            // bind beforeunload so user won't forget to submit response
            if (options.responseId.length > 0 && !options.submitted) {
                jQuery(window).bind('beforeunload', this.beforeUnload);
            }

            this.listenTo(this, 'render', this.render);
        },
        beforeUnload: function() {
            return 'Your work has been saved, ' +
                'but you have not submitted your response.';
        },
        busy: function(elt) {
            var parent = jQuery(elt).parents('.group-header')[0];
            elt = jQuery(parent).find('a.toggle-feedback .glyphicon');
            jQuery(elt).removeClass('glyphicon-pencil glyphicon-plus');
            jQuery(elt).addClass('glyphicon-repeat spin');
        },
        idle: function(elt) {
            var parent = jQuery(elt).parents('.group-header')[0];
            elt = jQuery(parent).find('a.toggle-feedback .glyphicon');
            jQuery(elt).removeClass('glyphicon-repeat spin');
            jQuery(elt).addClass('glyphicon-pencil');
        },
        onSaveFeedback: function(evt) {
            var self = this;
            evt.preventDefault();
            self.busy(evt.currentTarget);

            // change the feedback icon to a progress indicator
            var frm = jQuery(evt.currentTarget).parents('form')[0];

            jQuery.ajax({
                type: 'POST',
                url: frm.action,
                dataType: 'json',
                data: jQuery(frm).serializeArray(),
                success: function(json) {
                    // rerender the form based on the return context
                    var username = jQuery(frm).attr('data-username');
                    if (self.feedback[username].comment === undefined) {
                        self.feedbackCount++;
                    }
                    self.feedback[username].comment = {
                        'id': json.context.discussion.thread[0].id,
                        'content': json.context.discussion.thread[0].content
                    };
                    jQuery(frm).fadeOut('slow', function() {
                        self.trigger('render');
                    });
                },
                error: function() {
                    var msg = 'An error occurred while saving the feedback. ' +
                        'Please try again';
                    var pos = {
                        my: 'center', at: 'center',
                        of: jQuery('.container')
                    };
                    showMessage(msg, undefined, 'Error', pos);
                    self.idle(evt.currentTarget);
                }
            });
        },
        readyToSubmit: function() {
            return true;
        },
        onShowSubmitDialog: function(evt) {
            evt.preventDefault();

            var opts = {'show': true, 'backdrop': 'static'};

            if (this.readyToSubmit()) {
                jQuery('#submit-project').modal(opts);
            } else {
                jQuery('#cannot-submit-project').modal(opts);
            }
        },
        onSubmitResponse: function(evt) {
            evt.preventDefault();
            var frm = jQuery(this.el).find('.project-response-form')[0];
            jQuery.ajax({
                type: 'POST',
                url: frm.action,
                dataType: 'json',
                data: jQuery(frm).serializeArray(),
                success: function(json) {
                    jQuery(window).unbind('beforeunload');
                    window.location = json.context.project.url;
                },
                error: function() {
                    var msg = 'An error occurred while submitting your ' +
                        'response. Please try again';
                    var pos = {
                        my: 'center', at: 'center',
                        of: jQuery('.container')
                    };
                    showMessage(msg, undefined, 'Error', pos);
                }
            });
        },
        onToggleFeedback: function(evt) {
            evt.preventDefault();
            var q = jQuery(evt.currentTarget).attr('data-target');
            jQuery('#' + q).toggle();
        }
    });
}(jQuery));