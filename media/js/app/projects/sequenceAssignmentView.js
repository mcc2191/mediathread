/* global _: true, AssignmentView: true, updateUserSetting: true */
/* global MediaThread: true, tinymceSettings:true, tinymce: true */
/* global showMessage: true */
// jscs:disable requireCamelCaseOrUpperCaseIdentifiers

/**
 * Listens For:
 * Nothing
 *
 * Signals:
 * Nothing
 */

(function(jQuery) {
    var global = this;

    global.SequenceAssignmentView = AssignmentView.extend({
        events: {
            'click .submit-response': 'onSubmitResponse',
            'click .btn-show-submit': 'onShowSubmitDialog',
            'click .toggle-feedback': 'onToggleFeedback',
            'click .save-feedback': 'onSaveFeedback',
            'change textarea[name="comment"]': 'onChange',
            'keyup textarea[name="comment"]': 'onChange',
            'paste textarea[name="comment"]': 'onChange',
            'keyup input[name="title"]': 'onChange',
            'click .btn-save': 'onSaveProject'
        },
        initialize: function(options) {
            _.bindAll(this, 'render', 'onToggleFeedback',
                      'onShowSubmitDialog', 'onSubmitResponse',
                      'onSaveFeedback', 'onSaveFeedbackSuccess',
                      'onChange', 'onSaveProject', 'serializeData',
                      'isDirty', 'setDirty', 'beforeUnload',
                      'validTitle');

            AssignmentView.prototype.initialize.apply(this, arguments);

            var key = 'assignment_instructions_' + options.assignmentId;
            jQuery('#accordion').on('hidden.bs.collapse', function() {
                updateUserSetting(MediaThread.current_username, key, false);
            });

            jQuery('#accordion').on('shown.bs.collapse', function() {
                updateUserSetting(MediaThread.current_username, key, true);
            });

            var self = this;
            var settings = jQuery.extend(tinymceSettings, {
                height: '300',
                setup: function(ed) {
                    ed.on('change', function(e) {
                        self.setDirty(true);
                    });
                }
            });
            tinymce.init(settings);
        },
        beforeUnload: function() {
            // Check tinymce dirty state.
            // For some reason, the instance is not always current
            if (this.isDirty()) {
                return 'Changes to your project have not been saved.';
            }
        },
        readyToSubmit: function() {
            return true;
        },
        onChange: function() {
            this.setDirty(true);
            this.$el.find('.alert-success').fadeOut();
        },
        onSaveFeedbackSuccess: function(frm, json) {
            this.$el.find('.alert-success').show();
            var today = Date().toLocaleString();
            var dataId = 'feedback-date-' + this.responseId;
            this.$el.find('span[data-id=' + dataId + ']').html(today);
        },
        serializeData: function() {
            var q = '[name="title"], [name="body"]';
            return this.$el.find(q).serializeArray();
        },
        isDirty: function() {
            return tinymce.activeEditor.isDirty();
        },
        setDirty: function(isDirty) {
            var $elt = this.$el.find('.btn-save');

            if (isDirty) {
                $elt.text('Save');
            } else {
                tinymce.activeEditor.isNotDirty = true;
                $elt.text('Saved');
            }
        },
        validTitle: function() {
            var $title = this.$el.find('input.project-title').first();
            var value = $title.val();
            if (!value || value.length < 1) {
                showMessage(
                    'Please specify a title for your response',
                    null, 'Error');
                $title.focus();
                return false;
            }
            return true;
        },
        onSaveProject: function() {
            tinymce.activeEditor.save();

            if (!this.validTitle()) {
                return false;
            }

            var $saveButton = this.$el.find('.btn-save');
            $saveButton.attr('disabled', 'disabled')
                .text('Saving...')
                .addClass('saving');

            var self = this;
            jQuery.ajax({
                type: 'POST',
                url: '/project/save/' + this.responseId + '/',
                data: this.serializeData(),
                dataType: 'json',
                error: function() {
                    $saveButton.removeAttr('disabled')
                        .text('Save').removeClass('saving');
                    showMessage('There was an error saving your project.',
                                null, 'Error');
                },
                success: function(json, textStatus, xhr) {
                    if (json.status === 'error') {
                        showMessage(json.msg, null, 'Error');
                    } else {
                        self.setDirty(false);
                    }
                    $saveButton.removeAttr('disabled')
                        .removeClass('saving', 1200, function() {
                            jQuery(self).text('Saved'); });
                }
            });

            return true;
        }
    });
}(jQuery));
